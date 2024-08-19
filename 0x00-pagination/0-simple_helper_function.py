#!/usr/bin/env python3
"""Pagination:
is the process of separating print or digital content into discrete pages."""

from typing import Tuple


def index_range(page: int = 0, page_size: int = 0) -> Tuple[int, int]:
    """The function should return a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters."""
    start = (page - 1) * page_size
    return ( start,  start + page_size)
