"""
    You are given an M by N matrix consisting of booleans that represents a board.
    Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

    Given this matrix, a start coordinate, and an end coordinate, return the minimum number
    of steps required to reach the end coordinate from the start. If there is no possible path, then return null.
    You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

    For example, given the following board:

    [[f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]]

    and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7,
    since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

def shortest_path(M, N, matrix, start, end, count):
    if count == M*N:
        return 1
    if start == end:
        return 0
    left = -1
    right = -1
    up = -1
    down = -1
    if start[0] > 0 and matrix[start[0]-1][start[1]] == False:
        up = 1 + shortest_path(M, N, matrix, (start[0]-1, start[1]), end, count+1)
    if start[0] < M-1 and matrix[start[0]+1][start[1]] == False:
        down = 1 + shortest_path(M, N, matrix, (start[0]+1, start[1]), end, count+1)
    if start[1] > 0 and matrix[start[0]][start[1]-1] == False:
        left = 1 + shortest_path(M, N, matrix, (start[0], start[1]-1), end, count +1)
    if start[1] < N-1 and matrix[start[0]][start[1]+1] == False:
        right = 1 + shortest_path(M, N, matrix, (start[0], start[1]+1), end, count +1)
    res = [left, right, up, down]
    res.sort()
    for i in range(len(res)):
        if res[i] != -1:
            return res[i]

def min_steps(M, N, matrix, start, end):
    return shortest_path(M, N, matrix, start, end, 0)

print(min_steps(4,4,[[False, False, False, False],[True, True, False, True],[False, False, False, False],[False, False, False, False]], (3,0), (0,0)))
