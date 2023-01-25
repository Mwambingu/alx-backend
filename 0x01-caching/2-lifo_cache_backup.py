#!/usr/bin/env python3
"""
Contains a class that represents
a LIFO Caching system."""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ A class that represents a LIFO
    caching system
    """

    def __init__(self):
        """Initializes an instance of the LIFOCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns key-values to the dictionary
        cache_data"""
        cache_size = len(self.cache_data)
        item_keys = list(self.cache_data.keys())

        if key and item:
            if cache_size == BaseCaching.MAX_ITEMS and key not in item_keys:
                last_key, last_item = self.cache_data.popitem()
                print("DISCARD: {}".format(last_key))
                self.cache_data[key] = item

            elif key in item_keys:
                self.cache_data.pop(key)
                self.cache_data[key] = item

            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Retrieves value from dictionary using
        given key.
        Returns None if key or value doesn't exist"""
        if not key or not self.cache_data[key]:
            return None
        return self.cache_data[key]
