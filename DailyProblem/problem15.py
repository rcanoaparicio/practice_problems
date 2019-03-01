"""
    Given a stream of elements too large to store in memory,
    pick a random element from the stream with uniform probability.
"""
import random

def pick_rand_element_v0(elements_stream):
    return elements_stream[random.randint(0, len(elements_stream)-1)]

def pick_rand_element_v1(elements_stream):
    max_rand = 0
    rand = 0
    res = None
    for e in elements_stream:
        rand = random.uniform(0,1)
        if rand > max_rand:
            max_rand = rand
            res = e
    return res


n = 10000000

test = [0,0,0,0,0,0,0,0,0,0]

for i in range(n):
    test[pick_rand_element_v0([0,1,2,3,4,5,6,7,8,9])] += 1

print(test)

test = [0,0,0,0,0,0,0,0,0,0]

for i in range(n):
    test[pick_rand_element_v1([0,1,2,3,4,5,6,7,8,9])] += 1

print(test)
