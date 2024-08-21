#!/usr/bin/env python3

"""
What LRU means: LRU, or "Least Recently Used,"
is a more sophisticated (developed) cache eviction (pop) policy
that tracks the order of data usage.
When the cache is full,
the data that has not been accessed for the longest time is evicted (poped) first.
This policy is particularly effective in scenarios where
the most recently used data is likely to be accessed again soon.
"""

from base_caching import BaseCaching
import datetime

class LRUCache(BaseCaching):
    """Least Recently Used
        has not been accessed for the longest time
        is evicted (poped/ deleted/ removed) first
        """
    def __init__(self):
        super().__init__()
        self.order_time = datetime.datetime.now().isoformat()
        self.LRU_CACHE = {}

    def put(self, key, item):
        if not ( key is None or item is None):
            # if len(self.cache_data) == self.MAX_ITEMS:
            #     oldest_date = min(self.LRU_CACHE.keys())
            #     oldest_key =  self.LRU_CACHE.pop(oldest_date)
            #     if not self.cache_data.get(key):
            #         print('DISCARD: ', oldest_key)
            #     del self.cache_data[oldest_key]

            self.cache_data[key] = item
            date = datetime.datetime.now().isoformat()
            self.LRU_CACHE[date] = key

                
    def get(self, key):
        if self.cache_data.get(key):
            for time , k in self.LRU_CACHE.items():
                if k == key:
                    del self.LRU_CACHE[time]
                    updated_date = datetime.datetime.now().isoformat()
                    self.LRU_CACHE[updated_date] = k
                    return self.cache_data.get(key)
        return None

# print(datetime.datetime.now().isoformat())
# print(datetime.datetime.now().isoformat())
# print(datetime.datetime.now().isoformat())
# output
# 2024-08-20T14:31:44.864894
# 2024-08-20T14:31:44.865653
# 2024-08-20T14:31:44.865661
