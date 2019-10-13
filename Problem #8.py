# Problem 8
#
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# Solution


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def unival_tree_counter(node):
    count = 0
    if node.left is None and node.right is None:
        count += 1
    elif node.left is not None and node.right is not None:
        if node.left.val == node.right.val:
            count += 1
    if node.left is not None:
        count += unival_tree_counter(node.left)
    if node.right is not None:
        count += unival_tree_counter(node.right)
    return count
