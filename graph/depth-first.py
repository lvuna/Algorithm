from utils.create_graph import *
from random import choice
import string
import time

"""Implementations of Depth first search on a finite graph
   Note:
        Distance has been used as discover time here
        f_time refers to finish time
"""

# Global discover_time counter
D_COUNTER = 0


def depth_first_search(graph: Graph, root: Node=None) -> None:
    """
    This is a general approach depth first search, when working with topological sort,
    we can optimize it to achieve better runtime, check optimize_dfs
    """
    # Initialize the frontier, reset all nodes and reset counter
    if root is not None:
        frontier = [root]
    else:
        frontier = []
    global D_COUNTER
    D_COUNTER = 0
    for node in graph.node:
        node.parent = None
        node.distance = float("inf")
        node.f_time = float("inf")
        node.color = "white"
        if node != root:
            frontier.append(node)
    for node in frontier:
        if node.color == "white":
            _depth_first(node)


def _depth_first(node: Node) -> None:
    global D_COUNTER
    D_COUNTER += 1
    node.distance = D_COUNTER
    node.color = "grey"
    for neighbour in node.neighbour:
        if neighbour.color == "white":
            neighbour.parent = node
            _depth_first(neighbour)
    D_COUNTER += 1
    node.f_time = D_COUNTER
    node.color = "black"


def optimize_dfs(graph: Graph) -> None:
    """optimizes depth first search specific for topological sort"""
    frontier = []
    global D_COUNTER
    D_COUNTER = 0
    for node in graph.node:
        node.parent = None
        node.distance = float("inf")
        node.f_time = float("inf")
        node.color = "white"
        frontier.append(node)

    arr = []
    for node in frontier:
        if node.color == "white":
            if not _optimize_df(node, arr):
                return

    result = ""
    for i in range(len(arr) - 1, 0, -1):
        node = arr[i]
        result += f'{node.name} -> '
    result += f'{arr[0].name}'
    print(result)


def _optimize_df(node: Node, arr: list) -> bool:
    global D_COUNTER
    D_COUNTER += 1
    node.distance = D_COUNTER
    node.color = "grey"
    for neighbour in node.neighbour:
        if neighbour.color == "white":
            neighbour.parent = node
            if not _optimize_df(neighbour, arr):
                return False
        elif neighbour.color == "grey":
            print("cycle exists, no arrangement is possible, terminating..")
            return False
    D_COUNTER += 1
    node.f_time = D_COUNTER
    node.color = "black"
    arr.append(node)
    return True


def topological_sort(graph: Graph) -> None:
    depth_first_search(graph)
    for edge in graph.edge:
        if is_back_edge(edge):
            print("cycle exists, no arrangement is possible, terminating..")
            return
    node_copy = []
    for node in graph.node:
        node_copy.append(node)

    node_copy.sort(reverse=True, key=tpg_sort_func)
    result = ""
    length = len(node_copy) - 1
    for i in range(length):
        node = node_copy[i]
        result += f'{node.name} -> '
    result += f'{node_copy[length].name}'
    print(result)


def is_back_edge(edge: Edge) -> bool:
    src = edge.src
    dst = edge.dst
    if is_ancestor(src, dst):
        return True
    return False


def is_ancestor(src: Node, dst: Node) -> bool:
    if dst.parent == src:
        return False
    while src is not None:
        if src == dst:
            return True
        src = src.parent
    return False


def tpg_sort_func(node: Node) -> bool:
    return node.f_time


def optimized_topological_sort(graph: Graph) -> None:
    optimize_dfs(graph)


def generate_random_name(n: int) -> list:
    ret = []
    all_char = string.ascii_letters
    for _ in range(n):
        word = ""
        for _ in range(6):
            word += choice(all_char)
        ret.append(word)
    return ret


if __name__ == "__main__":
    graph1 = Graph()
    num = 30000
    arr = generate_random_name(num)
    graph1.random_generate(arr, num)
    start = time.time()
    topological_sort(graph1)
    end = time.time()
    print(f'Normal tps: {end - start}')
    o_start = time.time()
    optimized_topological_sort(graph1)
    o_end = time.time()
    print(f'Optimized tps: {o_end - o_start}')
