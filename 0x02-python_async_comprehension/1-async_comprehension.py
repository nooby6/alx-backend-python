#!/usr/bin/env python3
"""Contains an async comprehension"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension for an async generator

    Returns:
        list of random floats
    """
    return [i async for i in async_generator()]
