"""All the helper functions of avl_tree implementation"""
from bst_tree import TreeNode
from avl_tree import AvlNode


# ***************The start of all rotation methods********************
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
# ***************The end of all rotation methods********************


def height(node: "TreeNode") -> int:
    """Return the height of the tree"""
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return 1 + max(height(node.left), height(node.right))
