#!/usr/bin/python3

'''
Basic Caching in python
'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Basic Cache'''
    def __init__(self):
        '''Initialize cache'''
        super().__init__()

    def put(self, key, item):
        '''Put into cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Get from cache'''
        if key is None:
            return None
        return self.cache_data.get(key)
