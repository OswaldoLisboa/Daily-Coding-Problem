# Problem 3
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# Solution:


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def close_parenthesis(s):
    length = 0
    parenthesis = 0
    for i in s:
        if i == '(':
            parenthesis += 1
        if i == ')' and parenthesis >= 1:
            parenthesis -= 1
        if i == ')' and parenthesis < 1:
            parenthesis -= 1
            return length + 1
        length += 1


def serialize(node):
    s = ''
    s += '(' + node.val + ':'
    if node.left is not None:
        s += serialize(node.left) + ','
    else:
        s += 'None,'
    if node.right is not None:
        s += serialize(node.right)
    else:
        s += 'None'
    s += ')'
    return s


def deserialize(s):
    node = Node('placeholder')
    i = 1
    while i < len(s):
        if s[i] == ':':
            node.val = s[1:i]
            i += 1
            if s[i] == '(':
                node.left = deserialize(s[i:])
                i += close_parenthesis(s[i:]) + 1
            else:
                i += 5
            if s[i] == '(':
                node.right = deserialize(s[i:])
                i += close_parenthesis(s[i:]) + 1
            else:
                i += 5
            break
        i += 1
    return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'