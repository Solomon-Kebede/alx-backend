#!/usr/bin/python3


'''
LFU Caching in python
'''


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
    LFU Cache System
    '''
    def __init__(self):
        '''Initialize cache'''
        super().__init__()
        self.store1 = {}

    def put(self, key, item):
        '''Put into cache'''
        if key is not None and item is not None:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                if key not in self.store1.keys():
                    self.store1[key] = 0
                    self.cache_data[key] = item
                else:
                    self.store1[key] += 1
                    self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.store1:
                    lfu_val = min(self.store1.values())
                    lfu_key = list(
                        self.store1.keys()
                        )[list(self.store1.values()).index(lfu_val)]
                    del self.cache_data[lfu_key]
                    print(f'DISCARD: {lfu_key}')
                    lru_key_value = self.store1[lfu_key]
                    del self.store1[lfu_key]
                    self.store1[key] = 0
                    self.cache_data[key] = item
                else:
                    self.store1[key] += 1
                    self.cache_data[key] = item

    def get(self, key):
        '''Get from cache'''
        if key is None:
            return None
        if key in self.store1.keys():
            self.store1[key] += 1
        return self.cache_data.get(key)
