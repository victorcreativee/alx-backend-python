#!/usr/bin/env python3
"""
This module provides a higher-order function that
multiplies a float by a multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        its product with multiplier.
    """
    return lambda x: x * multiplier
