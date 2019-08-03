"""Visualization of disjoint set using forest structure"""

from numbers import Number
from random import randint
import time


class TreeNode:

    def __init__(self, key: Number) -> None:
        self.key = key
        self.parent = None
        self.height = 0
        self.children = []

    def __eq__(self, other) -> bool:
        return self is other

    def __str__(self) -> str:
        parent = None
        if self.parent is not None:
            parent = self.parent.key
        result = f'key: {self.key}, parent: {parent}'
        return result


class DisjointSet:
    """Implementation of the disjoint set"""

    def __init__(self, method) -> None:
        self.nodes = []
        self.union_method = method

    def add_node(self, node: "TreeNode") -> None:
        self.nodes.append(node)

    def union(self, index1, index2) -> None:
        if index1 >= len(self.nodes) or index2 >= len(self.nodes):
            raise IndexError("Index out of bound")
        self.union_method(self.nodes[index1], self.nodes[index2])

    def random_union(self) -> None:
        index1 = randint(0, len(self.nodes) - 1)
        index2 = randint(0, len(self.nodes) - 1)
        while index2 == index1:
            index2 = randint(0, len(self.nodes) - 1)
        self.union_method(self.nodes[index1], self.nodes[index2])

    def visualize(self) -> None:
        for node in self.nodes:
            print(node)


def find(node: "TreeNode") -> "TreeNode":
    while node.parent is not None:
        node = node.parent
    return node


# No heuristic are used in this union method
def union(node1: "TreeNode", node2: "TreeNode") -> None:
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        root1.children.append(root2)
        if root1.height == root2.height:
            root1.height += 1
        elif root1.height < root2.height:
            root1.height = root2.height + 1
        root2.parent = root1


# Utilizes weighted union heuristics to reduce time complexity
def wu_union(node1: "TreeNode", node2: "TreeNode") -> None:
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if root1.height > root2.height:
            root1.children.append(root2)
            root2.parent = root1
        elif root1.height == root2.height:
            root1.children.append(root2)
            root1.height += 1
            root2.parent = root1
        else:
            root2.children.append(root1)
            root1.parent = root2


def create_nodes(argv, d_set: "DisjointSet") -> None:
    for arg in argv:
        new_node = TreeNode(arg)
        d_set.add_node(new_node)


def test_runtime(union_method, union_method_name, num_elements, num_union) -> None:
    ds = DisjointSet(union_method)
    num_list = []
    for i in range(num_elements):
        num_list.append(i)

    create_nodes(num_list, ds)
    start = time.time()
    for _ in range(num_union):
        ds.random_union()
    end = time.time()
    take = end - start
    print(f'union method: {union_method_name}, num_union: {num_union}, time: {take}')


if __name__ == "__main__":
    test_runtime(union, "union", 1000000, 600000)
    test_runtime(wu_union, "wu_union", 1000000, 600000)
