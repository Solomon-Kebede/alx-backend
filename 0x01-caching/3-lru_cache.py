#!/usr/bin/python3


'''
LRU Caching in python
'''


from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LIFO Cache'''
    def __init__(self):
        '''Initialize cache'''
        super().__init__()
        self.count = 0
        self.store1 = {}
        self.store2 = {}

    def put(self, key, item):
        '''Put into cache'''
        if key is not None and item is not None:
            # print(self.cache_data)
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.store1[key] = self.count
                self.store2[self.count] = key
                self.count += 1
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.store1:
                    lru_key = self.store2.get(min(self.store2.keys()))
                    del self.cache_data[lru_key]
                    print(f'DISCARD: {lru_key}')
                    lru_key_value = self.store1[lru_key]
                    del self.store1[lru_key]
                    del self.store2[lru_key_value]
                    self.store1[key] = self.count
                    self.store2[self.count] = key
                    self.count += 1
                    self.cache_data[key] = item
                else:
                    # self.queue.append(key)
                    key_value = self.store1[key]
                    del self.store1[key]
                    del self.store2[key_value]
                    self.store1[key] = self.count
                    self.store2[self.count] = key
                    self.count += 1
                    self.cache_data[key] = item

    def get(self, key):
        '''Get from cache'''
        if key is None:
            return None
        return self.cache_data.get(key)
