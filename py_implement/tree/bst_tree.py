"""The binary search tree implementation, avl included"""
from numbers import Number
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
        pred = predecessor(target)
        target.key = pred.key
        target.value = pred.value
        parent_delete(pred.parent, pred)


def predecessor(target: "TreeNode") -> "TreeNode":
    """Find the predecessor of the target"""
    node = target.right
    while node.left is not None:
        node = node.left
    return node


def parent_delete(parent: "TreeNode", target: "TreeNode", childen: "TreeNode"=None) -> None:
    if parent.left is None:
        if childen is None:
            parent.right = None
        else:
            parent.right = childen
    elif parent.right is None:
        if childen is None:
            parent.left = None
        else:
            parent.left = childen
    elif parent.left.key == target.key:
        if childen is None:
            parent.left = None
        else:
            parent.left = childen
    else:
        if childen is None:
            parent.left = None
        else:
            parent.right = childen


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
