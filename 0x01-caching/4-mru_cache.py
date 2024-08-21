#!/usr/bin/env python3

"""

What MRU means: MRU, or "Most Recently Used,"
is the opposite of LRU. In MRU,
the data that was most recently used is the first to be removed
when the cache needs space.
This policy is less common and is used in specific situations
where recently accessed data is less likely to be used again.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    Mostst Recently Used
    is the first to be removed
    """
    def __init__(self):
        """overide cache_data, make it OrderdDict to handle insertion order"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add item and consider update value for exist key as accessed one"""
        if not (key is None or item is None):
            if key in self.cache_data.keys():
                del self.cache_data[key]

            if len(self.cache_data) == self.MAX_ITEMS:
                old_key, old_value = self.cache_data.popitem(last=True)
                print('DISCARD: ', old_key)

            self.cache_data[key] = item
            # now it's consider last added
            # the next ime if we want to delete someitem it will be this

    def get(self, key):
        """retrive item, update its insertion order by pop, insert it again"""
        if self.cache_data.get(key):
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
