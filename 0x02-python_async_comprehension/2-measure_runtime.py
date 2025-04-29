#!/usr/bin/env python3
"""Measure runtime module"""

import asyncio
import time
import importlib


async_comprehension = importlib.import_module("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime to run async_comprehension four times in parallel."""
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.perf_counter()
    return end - start
