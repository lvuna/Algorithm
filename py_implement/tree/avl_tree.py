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
        if other is None:
            return False
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


def left_rotate(node: "AvlNode") -> None:
    # set up node
    rotate_node = node.right

    # change the parent
    rotate_node.parent = node.parent
    if node.parent is not None:
        if node.parent.left == node:
            node.parent.left = rotate_node
        else:
            node.parent.right = rotate_node

    # update node's right children
    node.right = rotate_node.left
    if rotate_node.left is not None:
        rotate_node.left.parent = node.right

    # rotate node
    rotate_node.left = node
    node.parent = rotate_node


def right_rotate(node: "AvlNode") -> None:
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


def left_right_rotate(node: "AvlNode") -> None:
    first_node = node.left
    second_node = node.left.right
    left_rotate(node.left)
    right_rotate(node)
    update_balance(first_node, second_node, node)


def right_left_rotate(node: "AvlNode") -> None:
    first_node = node.right
    second_node = first_node.left
    right_rotate(node.right)
    left_rotate(node)
    update_balance(first_node, second_node, node)


def update_balance(*argv) -> None:
    for node in argv:
        node.balance = height(node.right) - height(node.left)


def height(node: "AvlNode") -> int:
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return 1 + max(height(node.left), height(node.right))


# To be implemented
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


def predecessor(target: "AvlNode") -> "AvlNode":
    """Find the predecessor of the target"""
    node = target.right
    while node.left is not None:
        node = node.left
    return node


def parent_delete(parent: "AvlNode", target: "AvlNode", children: "AvlNode"=None) -> None:
    if parent.left is None:
        if children is None:
            parent.right = None
        else:
            parent.right = children
    elif parent.right is None:
        if children is None:
            parent.left = None
        else:
            parent.left = children
    elif parent.left.key == target.key:
        if children is None:
            parent.left = None
        else:
            parent.left = children
    else:
        if children is None:
            parent.left = None
        else:
            parent.right = children


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
