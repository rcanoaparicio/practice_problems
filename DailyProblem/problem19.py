"""
    Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
    For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
    In this example, assume nodes with the same value are the exact same node objects.
    Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

def intersection(M, N):
    values = []
    e = M.first_node
    while e:
        values.append(e.value)
        e = e.next
    e = N.first_node
    while e:
        if e.value in values:
            return e
    return false
