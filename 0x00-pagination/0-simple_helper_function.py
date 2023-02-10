#!/usr/bin/env python3
"""
Return a tuple of size two containing a
start index and an end index corresponding
to the range of indexes to return in a list
for those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
	"""
	Return a tuple of size two containing a
	start index and an end index corresponding
	to the range of indexes to return in a list
	for those particular pagination parameters.
	"""
	return (page_size * (page-1), page_size * page)
