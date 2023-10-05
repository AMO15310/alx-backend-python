#!/usr/bin/env python3
"""Function that takes a list and returns its sum """

from typing import List,Union 

def sum_mixed_list(mxd_lst: List[Union[int,float]]) -> float:
    """Takes a list of floats and integers as argument and returns their sum as float"""
    return float(sum(mxd_lst))
