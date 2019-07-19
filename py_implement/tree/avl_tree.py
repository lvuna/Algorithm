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

    def __eq__(self, other) -> bool:
        return self.balance == other.balance and self.key == other.key and self.value == other.value


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
        # Left rotate
        if node.left.balance == -1:
            left_rotate(node)
        elif node.left.balance == 1:
            left_right_rotate(node)
    elif node.balance == +2:
        if node.right.balance == 1:
            right_rotate(node)
        elif node.right.balance == -1:
            right_left_rotate(node)


def left_rotate(node: "AvlNode") -> None:
    # set up node
    rotate_node = node.left

    # change the parent
    rotate_node.parent = node.parent
    if node.parent is not None:
        if node.parent.left == node:
            node.parent.left = rotate_node
        else:
            node.parent.right = rotate_node

    # update node's left children
    node.left = rotate_node.right
    if rotate_node.right is not None:
        rotate_node.right.parent = node.left

    # rotate node
    rotate_node.right = node
    node.parent = rotate_node
    rotate_node.balance = node.balance = 0


def right_rotate(node: "AvlNode") -> None:
    pass


def left_right_rotate(node: "AvlNode") -> None:
    pass


def right_left_rotate(node: "AvlNode") -> None:
    pass


# To be implemented
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
    node2 = AvlNode(4)
    node3 = AvlNode(3)
    node4 = AvlNode(2)
    node5 = AvlNode(1)
    test_AVL.insert(node1)
    test_AVL.insert(node2)
    test_AVL.insert(node3)
    test_AVL.insert(node4)
    test_AVL.insert(node5)
    visualize(test_AVL.root)
