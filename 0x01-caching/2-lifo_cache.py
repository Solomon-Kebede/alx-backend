#!/usr/bin/python3

'''
LIFO Caching in python
'''


from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO Cache'''
    def __init__(self):
        '''Initialize cache'''
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        '''Put into cache'''
        if key is not None and item is not None:
            # print(self.cache_data)
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.queue.append(key)
                self.cache_data[key] = item
                self.last_key = key
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.queue:
                    lifo_key = self.queue.pop()
                    self.queue.append(key)
                    del self.cache_data[lifo_key]
                    print(f'DISCARD: {lifo_key}')
                    self.cache_data[key] = item
                else:
                    self.queue.append(key)
                    self.cache_data[key] = item

    def get(self, key):
        '''Get from cache'''
        if key is None:
            return None
        return self.cache_data.get(key)
