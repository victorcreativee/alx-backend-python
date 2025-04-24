#!/usr/bin/env python3
"""
This module provides a function that returns a key-value pair tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the second element is the square of v.

    Args:
        k (str): The key.
        v (int or float): The value to square.

    Returns:
        Tuple[str, float]: A tuple (k, v^2 as float)
    """
    return (k, float(v ** 2))
