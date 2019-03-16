"""
    A builder is looking to build a row of N houses that can be of K different colors.
    He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

    Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
    return the minimum cost which achieves this goal.
"""

def helper(i, last_j, N, K, M, sum, prices):
    if i == N:
        prices.append(sum)
    else:
        for j in range(K):
            if last_j != j:
                helper(i+1, j, N, K, M, sum + M[j][i], prices)

def minimum_cost(N, K, M):
    arr = []
    res = 0
    for j in range(K):
        helper(1, j, N, K, M, M[j][0], arr)
    res = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < res:
            res = arr[i]

    return res

test = []
test.append([3,3,3,3,3,3,3,3])
test.append([3,3,3,3,3,3,3,3])
test.append([5,5,5,5,5,5,5,5])
test.append([3,3,3,3,3,3,3,3])
test.append([1,1,1,1,1,1,1,1])

print(minimum_cost(len(test[0]),len(test), test))
