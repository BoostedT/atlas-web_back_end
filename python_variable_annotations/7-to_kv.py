#!/usr/bin/env python3
"""task 7 to_kv.py"""

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key-value pair to a tuple.
    The value must be an integer or a float.
    """
    return (k, float(v**2))
