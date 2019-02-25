def staircase(n, v, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    res = 0
    for val in v:
        if memo[n-val] == 0:
            memo[n-val] = staircase(n-val, v, memo)
        res += memo[n-val]
    return res

n = 1000
memo = [0 for _ in range(n+1)]
print(staircase(n, [1, 2], memo))
