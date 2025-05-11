#!/usr/bin/env python3
"""Task Async Comprehension"""

from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Async Comprehension that returns a list of 10 random numbers"""
    return [i async for i in async_generator()]