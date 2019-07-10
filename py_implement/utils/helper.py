from typing import List
from random import randint
"""Helper function goes here"""


def choose_index(max: int) -> List[int]:
    src = randint(0, max)
    dst = randint(0, max)
    while dst == src:
        dst = randint(0, max)
    return [src, dst]
