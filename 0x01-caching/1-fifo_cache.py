#!/usr/bin/env python3

"""
What FIFO means: -> oooo o -> 
FIFO, or "First In, First Out,"
is a straightforward cache eviction policy
where the oldest data in the cache is removed first
when new data needs to be stored.
It's analogous to a queue, where the first element added is the first to be removed. 
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """First In, First Out"""
    ORDER = 0
    fifo_cash = {} 

    # to store {order: key}
    # then we can retrive the target key from the minimum order
    # then we delete the value that match that key from our original data_cach
    # so the flowchart will be as the following:
    # key = fifo_cach.get(min(order))
    # del data_cach.get(key)

    def put(self, key, item):
        """put method"""
        if not (key is None or item is None):
            self.ORDER += 1
 
            if len(self.cache_data) == self.MAX_ITEMS:
                order = self.fifo_cash.keys()
                first_in = min(order)
                target_key = self.fifo_cash.pop(first_in)
                print(f'DISCARD: {target_key}')
                del self.cache_data[target_key]

            self.cache_data[key] = item
            self.fifo_cash[self.ORDER] = key



    def get(self, key):
        """get method"""
        return self.cache_data.get(key)
