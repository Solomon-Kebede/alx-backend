#!/usr/bin/python3

'''
FIFO Caching in python
'''


from collections import deque

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO Cache'''
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
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.queue:
                    fifo_key = self.queue.popleft()
                    self.queue.append(key)
                    del self.cache_data[fifo_key]
                    print(f'DISCARD: {fifo_key}')
                    self.cache_data[key] = item
                else:
                    self.cache_data[key] = item

    def get(self, key):
        '''Get from cache'''
        if key is None:
            return None
        return self.cache_data.get(key)
