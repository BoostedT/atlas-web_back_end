#!/usr/bin/env python3
"""Task wait_random"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps wait_random with the given max_delay.
    """
    new_task = asyncio.create_task(wait_random(max_delay))
    return new_task
