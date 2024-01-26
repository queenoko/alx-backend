#!/usr/bin/env python3
"""This is a Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This function Retrieves the index range from a given page and page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)