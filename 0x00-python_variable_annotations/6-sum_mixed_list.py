#!/usr/bin/python3
"""Complex types - mixed list  """

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """ Return sum of list of floats """
    return sum(mxd_lst)