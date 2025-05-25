#!/usr/bin/env python3
"""task 0 0-basic_cache.py"""

from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
