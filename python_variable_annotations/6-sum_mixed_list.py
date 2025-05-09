#!/usr/bin/env python3
"""task 6 - sum_mixed_list"""

from typing import List,Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a mixed list of integers and floats"""
    return float(sum(mxd_lst))
