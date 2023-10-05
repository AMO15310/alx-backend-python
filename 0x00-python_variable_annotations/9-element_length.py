#!/usr/bin/env/python3
"""A function that returns a looped list """

from typing import Iterable, Sequence,List,Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence,int]]:
    """Return the values in the list and its length"""
    return [(i,len(i)) for i in lst]
