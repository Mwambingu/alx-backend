#!/usr/bin/env python3
"""
Contains a pagination helper function. That takes 2 integer args
and returns a tuple of size 2.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
