"""The binary search tree implementation"""
from numbers import Number
from typing import Union, List


class TreeNode:
    """The node in the tree"""

    parent: "TreeNode"
    left: "TreeNode"
    right: "TreeNode"

    def __init__(self, key: Number, value: Union[object, None]=None) -> None:
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def search(self, target: Number) -> object:
        if self.key == target:
            return self.key if self.value is None else self.value
        elif self.key < target and self.right is not None:
            return self.right.search(target)
        elif self.key > target and self.left is not None:
            return self.left.search(target)
        else:
            print("The target does not exist")
            return

    def __str__(self) -> str:
        left_children = None
        right_children = None
        if self.left is not None:
            left_children = self.left.key
        if self.right is not None:
            right_children = self.right.key
        result = f'Key:{self.key}, Children:{left_children} {right_children}'
        return result


class BinarySearchTree:
    """BST tree implementation"""

    root: "TreeNode"

    def __init__(self, root: "TreeNode") -> None:
        self.root = root

    def search(self, key: Number) -> object:
        return self.root.search(key)

    def insert(self, node: "TreeNode") -> None:
        return insert(self.root, node)

    def delete(self, key: Number) -> None:
        pass


def visualize(root: "TreeNode") -> None:
    print(root)
    if root.left is not None:
        visualize(root.left)
    if root.right is not None:
        visualize(root.right)


def insert(root: "TreeNode", node: "TreeNode") -> None:
    """Insert the node into BST."""
    if root.key <= node.key:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    elif root.key > node.key:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


if __name__ == "__main__":
    root_node = TreeNode(7)
    test_BST = BinarySearchTree(root_node)
    node1 = TreeNode(5)
    node2 = TreeNode(9)
    node3 = TreeNode(8)
    node4 = TreeNode(1)
    test_BST.insert(node1)
    test_BST.insert(node2)
    test_BST.insert(node3)
    test_BST.insert(node4)
    visualize(test_BST.root)
