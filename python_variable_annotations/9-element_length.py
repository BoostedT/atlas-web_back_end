#!/usr/bin/env python3
"""task 9 lets duck type an iterable object"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains the element and its length.
    """
    return [(i, len(i)) for i in lst]
