#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): List of float numbers.

    Returns:
        float: The sum of all floats in the list.
    """
    return sum(input_list)
