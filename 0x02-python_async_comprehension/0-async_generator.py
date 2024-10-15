#!/usr/bin/env python3
"""Contains an async generator function"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator that yields a random float between 0 and 10
    every second.
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
