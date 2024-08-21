#!/usr/bin/env python3

"""
What LIFO means: LIFO, or "Last In, First Out,"
is another simple cache eviction strategy
where the most recently added data is the first to be removed.
This approach is similar to a stack,
where the last element added is the first to be removed.
-> o oooo|
   o

   |
   V
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """First In, First Out"""
    def __init__(self):
        """overide cache_data, make it OrderdDict to handle insertion order"""
        super().__init__()
        self.order = 0
        self.lifo_cache = {}

    def put(self, key, item):
        """add item, omit update value, just consider its added order only"""
        if not (key is None or item is None):
            self.order += 1

            if len(self.cache_data) == self.MAX_ITEMS:
                order = self.lifo_cache.keys()
                first_in = max(order)
                target_key = self.lifo_cache.pop(first_in)
                print(f'DISCARD: {target_key}')
                del self.cache_data[target_key]

            self.cache_data[key] = item
            self.lifo_cache[self.order] = key

    def get(self, key):
        """get method"""
        return self.cache_data.get(key)
