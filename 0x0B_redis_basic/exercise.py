#!/usr/bin/env python3
from typing import Union
import redis
import uuid


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
