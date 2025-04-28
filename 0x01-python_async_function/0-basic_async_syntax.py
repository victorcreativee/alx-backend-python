#!/usr/bin/env python3
"""Module that contains wait_random coroutine"""
import asyncio
import random
from typing import Awaitable

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive),
    and returns the delay time.
    """
    delay = random.uniform(0, max_delay)  # random float between 0 and max_delay
    await asyncio.sleep(delay)             # asynchronously wait
    return delay
