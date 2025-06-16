#!/usr/bin/env python3
from typing import Union
import redis
from uuid import uuid4
from typing import Optional, Callable, Union


class Cache:
    def __init__(self):
        """Initialize Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a UUID key, store the data in Redis, and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)
