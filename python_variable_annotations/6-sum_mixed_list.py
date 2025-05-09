#!/usr/bin/env python3
"""task 6 - sum_mixed_list"""

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[float | int]]) -> float:
    """Returns the sum of a mixed list of integers and floats"""
    return float(sum(mxd_lst))
