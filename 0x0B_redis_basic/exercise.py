#!/usr/bin/env python3
"""Module for Redis cache with decorators to count calls and store history."""
from typing import Union
from functools import wraps
import redis
from uuid import uuid4
from typing import Optional, Callable, Union


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of calls to a method."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a method."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        results = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(results))
        return results

    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls to a method."""
    r = method.__self__._redis
    name = method.__qualname__

    inputs = r.lrange(f"{name}:inputs", 0, -1)
    outputs = r.lrange(f"{name}:outputs", 0, -1)

    print(f"{name} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{name}(*{inp.decode()}) -> {out.decode()}")


class Cache:
    """Initialize the Cache with a Redis connection and flush the database."""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a UUID key, store the data in Redis, and return the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, None]:
        """Retrieve data from Redis by key and apply a function if provided."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis by key."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis by key."""
        return self.get(key, fn=int)
