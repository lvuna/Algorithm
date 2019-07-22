from typing import List
from random import randint
from create_graph import Edge
"""Helper function goes here"""


def choose_index(maxnum: int) -> List[int]:
    src = randint(0, maxnum - 1)
    dst = randint(0, maxnum - 1)
    while dst == src:
        dst = randint(0, maxnum - 1)
    return [src, dst]


def is_infinity(distance: int) -> bool:
    return distance == float("inf")


def check_for_same_edge(edge1: "Edge", edge2: "Edge"):
    if edge1.src == edge2.src and edge1.dst == edge2.dst:
        return True
    else:
        return False
