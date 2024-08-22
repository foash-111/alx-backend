#!/usr/bin/env python3

"""
What LRU means: LRU, or "Least Recently Used,"
is a more sophisticated (developed) cache eviction (pop) policy
that tracks the order of data usage.
When the cache is full,
the data that has not accessed for the longest time is evicted (poped) first.
This policy is particularly effective in scenarios where
the most recently used data is likely to be accessed again soon.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Least Recently Used
        has not been accessed for the longest time
        is evicted (poped/ deleted/ removed) first
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
                old_key, old_value = self.cache_data.popitem(last=False)
                print('DISCARD:', old_key)

            self.cache_data[key] = item
            # now it's consider last added

    def get(self, key):
        """retrive item, update its insertion order by pop, insert it again"""
        if self.cache_data.get(key):
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
    # insert again to put access order in consider, cuz it's an OrederedDict()
            return value

        return None
