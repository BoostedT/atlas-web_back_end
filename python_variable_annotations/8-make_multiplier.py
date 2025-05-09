#!/usr/bin/env python3
""" task 8 float multiplier"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(number: float) -> float:
        """multiplies a number by multiplier"""
        return number * multiplier

    return multiply
