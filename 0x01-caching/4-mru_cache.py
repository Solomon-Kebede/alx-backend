#!/usr/bin/python3


'''
MRU Caching in python
'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    MRU Cache
    '''
    def __init__(self):
        '''Initialize cache'''
        super().__init__()
        self.store1 = {}
        self.count = 0

    def put(self, key, item):
        '''Put into cache'''
        if key is not None and item is not None:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.store1[key] = self.count
                self.count += 1
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.store1:
                    mru_val = max(self.store1.values())
                    mru_key = list(
                        self.store1.keys()
                        )[list(self.store1.values()).index(mru_val)]
                    del self.cache_data[mru_key]
                    print(f'DISCARD: {mru_key}')
                    del self.store1[mru_key]
                    self.store1[key] = self.count
                    self.count += 1
                    self.cache_data[key] = item
                else:
                    pass
                    self.store1[key] = self.count
                    self.count += 1
                    self.cache_data[key] = item

    def get(self, key):
        '''Get from cache'''
        if key is None:
            return None
        if key in self.store1.keys():
            self.store1[key] = self.count
            self.count += 1
        return self.cache_data.get(key)
