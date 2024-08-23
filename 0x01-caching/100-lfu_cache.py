#!/usr/bin/env/python3

"""

What LFU means: LFU, or "Least Frequently Used,"
is a cache eviction (deletion) policy that counts the frequency of data usage
and removes the data that has been accessed the least number of times.
This approach is useful
when access patterns are such that data accessed frequently in the past
will continue to be accessed frequently in the future.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Least Frequently Used"""
    def __init__(self):
        """overide cache_data, make it OrderdDict to handle insertion order"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.lfu_cache = {}

    
    def put(self, key, item):
        """put"""
        if not (key is None or item is None):
            if key in self.cache_data.keys():
                self.lfu_cache[key] += 1

            if len(self.cache_data) == self.MAX_ITEMS:
                mini = min(self.lfu_cache.values())
                temp_dict = OrderedDict()
                for k, v in self.lfu_cache.items():
                    if v == mini and k in self.cache_data.keys():
                        temp_dict[k] = self.cache_data[k]
                if len(temp_dict) != 0:
                    old_key, value = temp_dict.popitem(last=False)
                else:
                    old_key, value = self.cache_data.popitem(last=False)
                if old_key in self.cache_data.keys():
                    del self.cache_data[old_key]
                print('DISCARD:', old_key)

            self.cache_data[key] = item
            if not self.lfu_cache.get(key):
                self.lfu_cache[key] = 1       


    def get(self, key):
        if self.cache_data.get(key):
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            self.lfu_cache[key] += 1
            return value
        return None
