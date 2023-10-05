#!/usr/bin/env python3
"""Function that takes a string and an int or a float and returns a tupple from them"""

from typing import Tuple,Union

def to_kv(k:str, v:Union[int,float]) -> Tuple[str,float]:
    """Returns a tuple of a string and the square of the variable v as a float"""
    return (k, float(v * v))
