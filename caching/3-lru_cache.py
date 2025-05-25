#!/usr/bin/env python3
"""task 3 3-lru_cache.py"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                # Update the existing item
                self.cache_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the least recently used item
                lru_key = self.cache_order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            # Move the accessed item to the end of the cache order
            self.cache_order.remove(key)
            self.cache_order.append(key)
            return self.cache_data[key]
        return None
