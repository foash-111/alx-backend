#!/usr/bin/env python3
"""pagintaion, dealing with csv file"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def index_range(self, page: int = 0, page_size: int = 0) ->\
            Tuple[int, int]:
        """The function should return a tuple of size two
        containing a start index and an end index
        corresponding to the range of indexes to return
        in a list for those particular pagination parameters."""
        if page <= 0:
            raise IndexError('index error')
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 2) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)
        dataset = self.dataset()
        # print(type(range[0]))
        # print(type(len(dataset)))
        # return(dataset)

        if (start >= len(dataset)):
            return []
        return dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 2):
        """return dict of pagination discription"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)
        dataset = self.dataset()

        if (start >= len(dataset)):
            data = []
        else:
            data = dataset[start: end]

        prev_page = None
        next_page = None

        if page != 1:
            prev_page = page - 1

        total_pages = int(len(dataset) / page_size)

        if page < total_pages:
            next_page = page + 1

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

# ob = Server()
# print(ob.get_page())
