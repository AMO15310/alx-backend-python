#!/usr/bin/env python3
"""A function that takes a multiplier and returns another function which multiplies the multiplier with a variable """

from typing import Callable

def make_multiplier(multiplier:float) -> Callable[[float],float]:
    """Now we define the func which will be returned"""
    def multiplier_function(value:float) -> float:
        """Multiply the value with our multiplier value and return it as a float"""
        return value * multiplier
    return multiplier_function
