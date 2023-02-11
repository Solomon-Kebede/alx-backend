#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List, Dict
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns paginated page data depending on page and page_size"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        indice = index_range(page, page_size)
        return self.dataset()[indice[0]:indice[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Hypermedia pagination"""
        if page >= 2:
            prev_page = page - 1
        else:
            prev_page = None
        if self.get_page(page + 1, page_size) != []:
            next_page = page + 1
        else:
            next_page = None
        total_pages = math.ceil(len(self.dataset())/page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a
    start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    return (page_size * (page-1), page_size * page)
