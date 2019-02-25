"""
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
"""

def find_missing_int(arr):
    mem = {}
    for n in arr:
        if (n > 0):
            mem[n] = True
    i = 1
    while i < len(mem):
        if mem.get(i) == None:
            return i
        i += 1
    return i

print(find_missing_int([2, 4, -3, 1]))
print(find_missing_int([2, 3, -5]))
