#!/usr/bin/python3
"""
Contains a class that represents
a FIFO Caching system.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A class that represents a FIFO
    caching system
    """

    def __init__(self):
        """Initializes an instance of the FIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Assigns key-values to the dictionary
        cache_data"""
        cache_size = len(self.cache_data)
        item_keys = list(self.cache_data.keys())

        if key and item:
            if cache_size == BaseCaching.MAX_ITEMS and key not in item_keys:
                first_item = item_keys[0]
                self.cache_data.pop(first_item)
                print(f"DISCARD: {first_item}")
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves value from dictionary using
        given key.
        Returns None if key or value doesn't exist
        """
        if not key:
            return None
        if not self.cache_data[key]:
            return None
        return self.cache_data[key]
