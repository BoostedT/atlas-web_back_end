#!/usr/bin/env python3
"""task 3 3-hypermedia_del_pagination.py"""
import csv
import math
import os
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = os.path.join(os.path.dirname(__file__), "Popular_Baby_Names.csv")

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Get a deletion-resilient page of the dataset with metadata."""
        assert (
            isinstance(index, int) and index >= 0
        ), "index must be a non-negative integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page_size must be a positive integer"

        indexed_dataset = self.indexed_dataset()
        assert index < len(self.dataset()), "index out of range"

        data = []
        current_index = index

        while len(data) < page_size and current_index < len(self.dataset()):
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data,
        }
