"""
    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
    and deserialize(s), which deserializes the string back into the tree.

    For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize_help(root):
    if root != None:
        return root.val + ","+serialize_help(root.left)+","+serialize(root.right)
    else:
        return "None"

def serialize(root):
    return serialize_help(root)

def deserialize_help(arr, i):
    n = Node(arr[i])
    if arr[i+1] != "None":
        n.left, i = deserialize_help(arr, i+1)
    else:
        i += 1
    if arr[i+1] != "None":
        n.right, i = deserialize_help(arr, i+1)
    else:
        i+= 1
    return n, i


def deserialize(s):
    spl = s.split(",")
    if len(spl) < 3:
        return None
    res, _ = deserialize_help(spl, 0)
    return res

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
