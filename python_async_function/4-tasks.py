#!/usr/bin/env python3
"""Task wait_n"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create a list of tasks to spawn wait_random 
    n times with the specified max_delay.
    Return the list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
