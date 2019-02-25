"""
    Given an array of integers, return a new array such that each element at index i of the new array
    is the product of all the numbers in the original array except the one at i.
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].
    Follow-up: what if you can't use division?
"""
import time
from random import randint

def productArr(numbers):
    mult = 1
    result = []
    for i in range(len(result)):
        mult *= numbers[i]
    for i in range(len(numbers)):
        result.append(mult//numbers[i])
    return result

def productArr2(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(1)
        for j in range(len(numbers)):
            if i != j:
                result[i] *= numbers[j]
    return result

n = 10000
arr = []
for i in range(n):
    arr.append(1)

start = time.time()
res = productArr(arr)
end = time.time()
print("Execution 1:", end-start)

start = time.time()
res = productArr2(arr)
end = time.time()
print("Execution 2:", end-start)
