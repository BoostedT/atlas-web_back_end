#!/usr/bin/env python3
"""task 2 2-lifo_cache.py"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the last item in the cache
                oldest_key = self.cache_order.pop()
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
