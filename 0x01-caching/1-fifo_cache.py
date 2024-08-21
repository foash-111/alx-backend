#!/usr/bin/env python3

"""
What FIFO means: -> oooo o ->
FIFO, or "First In, First Out,"
is a straightforward cache eviction policy
where the oldest data in the cache is removed first
when new data needs to be stored.
It's analogous to a queue,
where the first element added is the first to be removed.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """First In, First Out"""
    # ORDER = 0
    # fifo_cache = {}
    # to store {order: key}
    # then we can retrive the target key from the minimum order
    # then we delete the value that match that key from our original data_cach
    # so the flowchart will be as the following:
    # key = fifo_cach.get(min(order))
    # del data_cach.get(key)

    def __init__(self):
        """
        Instead of using class-level variables (ORDER and fifo_cache),
        you should use instance variables initialized in the __init__ method.
        This prevents issues if multiple instances of FIFOCache are created.
        """
        super().__init__()
        self.order = 0
        self.fifo_cache = {}

    def put(self, key, item):
        """add item, omit update value, just consider its added order only"""
        if not (key is None or item is None):
            self.order += 1

            if len(self.cache_data) == self.MAX_ITEMS:
                order = self.fifo_cache.keys()
                first_in = min(order)
                target_key = self.fifo_cache.pop(first_in)
                print(f'DISCARD: {target_key}')
                del self.cache_data[target_key]

            self.cache_data[key] = item
            self.fifo_cache[self.order] = key

    def get(self, key):
        """get method"""
        return self.cache_data.get(key)
