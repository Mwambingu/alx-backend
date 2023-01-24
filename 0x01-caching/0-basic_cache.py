#!/usr/bin/python3
"""
Contains a Class BasicCache that
represents a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class represnting a caching system"""

    def __init__(self):
        """Initializes a caching system"""
        super().__init__()

    def put(self, key, item):
        """Assigns key-values to the dictionary
        cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves value from dictionary using
        given key.
        Returns None if key or value doesn't exist
        """
        if not key:
            return None

        if key not in self.cache_data:
            return None

        return self.cache_data[key]
