"""
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
    Given N, write a function that returns the number of unique ways you can climb the staircase.
    The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

    What if, instead of being able to climb 1 or 2 steps at a time,
    you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5},
    you could climb 1, 3, or 5 steps at a time
"""

def count(n, steps, memo):
    if n in memo:
        return memo[n]
    if n < 0:
        memo[n] = 0
        return 0
    if n == 0:
        memo[n] = 1
        return 1
    r = 0
    for step in steps:
        r += count(n-step, steps, memo)
    memo[n] = r
    return r

print(count(4, [1, 2], {}))
print(count(4, [1, 3, 5], {}))
print(count(5, [1, 3, 5], {}))
print(count(100, [1, 2, 3, 4, 6, 7, 8, 9, 11, 17, 13, 45, 23, 12, 14, 5, 6], {}))
