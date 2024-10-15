#!/usr/bin/env python3
"""Contains a method for measuring async generator/comprehension runtime"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime for 4 calls to async_comprehension

    Returns
        float: total runtime
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    done = time.time()

    return done - start
