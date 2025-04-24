#!/usr/bin/env python3
"""
This module provides a function to sum a list of mixed ints and floats.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of numbers.

    Returns:
        float: The sum of the list.
    """
    return sum(mxd_lst)
