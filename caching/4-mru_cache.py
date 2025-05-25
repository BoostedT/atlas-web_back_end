#!/usr/bin/env python3
"""task 4 4-mru_cache"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = {}
        self.most_recently_used = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.most_recently_used.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.most_recently_used.append(key)

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.most_recently_used.remove(key)
            self.most_recently_used.append(key)
            return self.cache_data[key]
        return None
