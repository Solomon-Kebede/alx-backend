#!/usr/bin/env python3
"""
3. Deletion-resilient hypermedia pagination
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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns paginated page data depending on page and page_size"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        indice = index_range(page, page_size)
        return self.dataset()[indice[0]:indice[1]]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Handle if between two queries, certain rows are removed
        from the dataset, the user does not miss items from dataset
        when changing page
        """
        if index is not None:
            assert index < len(self.__dataset)
            if index + 1 < len(self.__dataset):
                next_index = index + 1
            page = math.ceil(index/page_size)
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": self.get_page(page, page_size),
        }


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a
    start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    return (page_size * (page-1), page_size * page)
