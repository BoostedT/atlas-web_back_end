#!/usr/bin/env python3
"""Task Async generator"""

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Async generator that yields a random number every second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
