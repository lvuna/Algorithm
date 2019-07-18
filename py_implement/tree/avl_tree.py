"""Augmented bst_tree, where the height is balanced"""
from numbers import Number
from bst_tree import TreeNode, BinarySearchTree, visualize
from typing import Union


class AvlNode(TreeNode):
    """Node for AvlTree"""

    def __init__(self, key: Number, value: Union[object, None]=None) -> None:
        super().__init__(key, value)
        self.balance = 0

    def __str__(self) -> str:
        result = super().__str__()
        factor = f', Balance Factor:{self.balance}'
        result += factor
        return result


class AvlTree(BinarySearchTree):
    """Avl tree implementation"""

    def __init__(self, root: "AvlNode") -> None:
        super().__init__(root)

    def insert(self, node: "AvlNode") -> None:
        insert(self.root, node)
        fix_factor(node)

    def delete(self, key: Number) -> None:
        delete(self.root, key)


def insert(root: "AvlNode", node: "AvlNode") -> None:
    """Insert the node into BST."""
    if root.key <= node.key:
        if root.right is None:
            node.parent = root
            root.balance += 1
            root.right = node
        else:
            root.balance += 1
            insert(root.right, node)
    elif root.key > node.key:
        if root.left is None:
            node.parent = root
            root.balance -= 1
            root.left = node
        else:
            root.balance -= 1
            insert(root.left, node)


def fix_factor(node: "AvlNode") -> None:
    pass


def rotate(node: "AvlNode") -> None:
    pass


def delete(root: "AvlNode", key: Number) -> None:
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


def predecessor(target: "AvlNode") -> "AvlNode":
    """Find the predecessor of the target"""
    node = target.right
    while node.left is not None:
        node = node.left
    return node


def parent_delete(parent: "AvlNode", target: "AvlNode", childen: "AvlNode"=None) -> None:
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
    root_node = AvlNode(7)
    test_AVL = AvlTree(root_node)
    node1 = AvlNode(5)
    node2 = AvlNode(9)
    node3 = AvlNode(8)
    node4 = AvlNode(2)
    node5 = AvlNode(1)
    node6 = AvlNode(11)
    test_AVL.insert(node1)
    test_AVL.insert(node2)
    test_AVL.insert(node3)
    test_AVL.insert(node4)
    test_AVL.insert(node5)
    visualize(test_AVL.root)
