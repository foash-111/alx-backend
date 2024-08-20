#!/usr/bin/env python3
"""
    caching:
    stores a subset of data in a faster storage medium,
    typically RAM, to speed up data retrieval
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ caching system"""
    def put(self, key, item):
        """setattr"""
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """dict get method"""
        return self.cache_data.get(key)
