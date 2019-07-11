from typing import List
from random import randint
"""Helper function goes here"""


def choose_index(maxnum: int) -> List[int]:
    src = randint(0, maxnum - 1)
    dst = randint(0, maxnum - 1)
    while dst == src:
        dst = randint(0, maxnum - 1)
    return [src, dst]
