"""Augmented bst_tree, where the height is balanced"""
from numbers import Number
from bst_tree import BinarySearchTree, visualize, predecessor, parent_delete
from tree.helper import *
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

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.balance == other.balance and self.key == other.key


class AvlTree(BinarySearchTree):
    """Avl tree implementation"""

    def __init__(self, root: "AvlNode") -> None:
        super().__init__(root)

    def insert(self, node: "AvlNode") -> None:
        insert(self.root, node)
        fix_factor(node)
        self.update_root()

    def update_root(self) -> None:
        while self.root.parent is not None:
            self.root = self.root.parent

    def delete(self, key: Number) -> None:
        delete(self.root, key)


def insert(root: "AvlNode", node: "AvlNode") -> None:
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


# The below 2 functions are for fixing the factors for insertion with slight computation saving
def fix_factor(node: "AvlNode") -> None:
    """Fix the balance factor of each node"""
    while node.parent is not None:
        update_factor(node, node.parent)
        node = node.parent
        if node.balance == 0:
            # There is no need to fix further
            return
        elif node.balance > 1 or node.balance < -1:
            rotate(node)
            # Only 1 rotation is enough
            return


def update_factor(node: "AvlNode", parent: "AvlNode") -> None:
    if node == parent.left:
        parent.balance -= 1
    elif node == parent.right:
        parent.balance += 1


def rotate(node: "AvlNode") -> None:
    if node.balance == -2:
        # right rotate
        if node.left.balance == -1:
            rotated_node = node.left
            right_rotate(node)
            node.balance = rotated_node.balance = 0
        # left right rotate
        elif node.left.balance == 1:
            left_right_rotate(node)

    elif node.balance == +2:
        # left rotate
        if node.right.balance == 1:
            rotated_node = node.right
            left_rotate(node)
            node.balance = rotated_node.balance = 0
        # right left rotate
        elif node.right.balance == -1:
            right_left_rotate(node)


def delete(root: "AvlNode", key: Number) -> None:
    """Delete the node of given if it exists"""
    target = root.search(key)
    parent = target.parent
    if target is None:
        return
    if target.left is None and target.right is None:
        parent_delete(parent, target)
        update_balance_after_delete(parent)
    elif target.left is None and target.right is not None:
        parent_delete(parent, target, target.right)
        update_balance_after_delete(parent)
    elif target.right is None and target.left is not None:
        parent_delete(parent, target, target.left)
        update_balance_after_delete(parent)
    else:
        new_target = predecessor(target)
        target.key = new_target.key
        target.value = new_target.value
        parent_delete(new_target.parent, new_target)
        update_balance_after_delete(new_target.parent)


def update_balance_after_delete(node: "AvlNode") -> None:
    while node is not None:
        update_balance(node)
        if node.balance > 1 or node.balance < -1:
            rotate(node)
        node = node.parent


if __name__ == "__main__":
    root_node = AvlNode(2)
    test_AVL = AvlTree(root_node)
    node1 = AvlNode(1)
    node2 = AvlNode(5)
    node3 = AvlNode(4)
    node4 = AvlNode(6)
    node5 = AvlNode(3)
    node6 = AvlNode(7)
    node7 = AvlNode(10)
    node8 = AvlNode(8)
    test_AVL.insert(node1)
    test_AVL.insert(node2)
    test_AVL.insert(node3)
    test_AVL.insert(node4)
    test_AVL.insert(node5)
    test_AVL.insert(node6)
    test_AVL.insert(node7)
    test_AVL.insert(node8)
    test_AVL.delete(7)
    test_AVL.delete(5)
    visualize(test_AVL.root)
