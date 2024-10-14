#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    seconds and then returns the actual delay.

    Args:
        max_delay (int): The maximum delay time (default is 10 seconds).

    Returns:
        float: The random delay time waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

