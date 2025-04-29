#!/usr/bin/env python3
"""Async comprehension module"""
import importlib
from typing import List
async_generator = importlib.import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator and
    returns them as a list."""
    return [i async for i in async_generator()]
