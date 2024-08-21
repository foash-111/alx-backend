#!/usr/bin/env python3
"""
    caching:
    What a caching system is:
    A caching system is an optimization technique
    that stores a subset of data in a faster storage medium, typically RAM,
    to speed up data retrieval.
    It reduces the time it takes to access data that is frequently used
    by temporarily storing it closer to the processing unit.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ caching system"""
    def put(self, key, item):
        """add item, update its value if key exists"""
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """get item value if the exists or None if not"""
        return self.cache_data.get(key)
