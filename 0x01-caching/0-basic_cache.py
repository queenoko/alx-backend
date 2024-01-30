#!/usr/bin/env python3
"""This scipt is the Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This module Represents the object which allows storing and
    retrieval of items from dictionary.
    """
    def put(self, keyItem, item):
        """This adds an item in the cache.
        """
        if keyItem is None or item is None:
            return
        self.cache_data[keyItem] = item

    def get(self, keyItem):
        """Retrieves an item by key.
        """
        return self.cache_data.get(keyItem, None)