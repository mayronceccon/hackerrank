# https://www.hackerrank.com/challenges/list-comprehensions/problem


def sum_three_values(x, y, z, n):
   return [[x1, y1, z1] for x1 in range(x + 1) for y1 in range(y + 1) for z1 in range(z + 1) if x1 + y1 + z1 != n]


assert [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] == sum_three_values(1, 1, 1, 2)
assert [
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], 
    [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], 
    [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]
] == sum_three_values(2, 2, 2, 2)
