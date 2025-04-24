#!/usr/bin/env python3
"""
This module provides a function to return element lengths in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence items
         (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples (item, len(item))
    """
    return [(i, len(i)) for i in lst]
