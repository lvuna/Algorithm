"""The binary search tree implementation, avl included"""
from numbers import Number
from tree.helper import predecessor, parent_delete
from typing import Union


class TreeNode:
    """The node in the tree"""

    def __init__(self, key: Number, value: Union[object, None]=None) -> None:
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def search(self, target: Number) -> Union["TreeNode", None]:
        if self.key == target:
            return self
        elif self.key < target and self.right is not None:
            return self.right.search(target)
        elif self.key > target and self.left is not None:
            return self.left.search(target)
        else:
            print("The target does not exist")
            return

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.key == other.key

    def __str__(self) -> str:
        parent = None
        left_children = None
        right_children = None
        if self.left is not None:
            left_children = self.left.key
        if self.right is not None:
            right_children = self.right.key
        if self.parent is not None:
            parent = self.parent.key
        result = f'Key:{self.key}, Children:{left_children} {right_children}， Parent:{parent}'
        return result


class BinarySearchTree:
    """BST tree implementation"""

    def __init__(self, root: "TreeNode") -> None:
        self.root = root

    def search(self, key: Number) -> object:
        return self.root.search(key)

    def insert(self, node: "TreeNode") -> None:
        insert(self.root, node)

    def delete(self, key: Number) -> None:
        delete(self.root, key)


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
            node.parent = root
            root.right = node
        else:
            insert(root.right, node)
    elif root.key > node.key:
        if root.left is None:
            node.parent = root
            root.left = node
        else:
            insert(root.left, node)


def delete(root: "TreeNode", key: Number) -> None:
    """Delete the node of given if it exists"""
    target = root.search(key)
    parent = target.parent
    if target is None:
        return
    if target.left is None and target.right is None:
        parent_delete(parent, target)
    elif target.left is None and target.right is not None:
        parent_delete(parent, target, target.right)
    elif target.right is None and target.left is not None:
        parent_delete(parent, target, target.left)
    else:
        new_target = predecessor(target)
        target.key = new_target.key
        target.value = new_target.value
        parent_delete(new_target.parent, new_target)


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
    test_BST.delete(7)
    visualize(test_BST.root)
