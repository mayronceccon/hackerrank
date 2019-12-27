# https://www.hackerrank.com/challenges/triangle-quest-2/problem

from functools import reduce
import operator


def triangle_palindromic(n):
    s = []
    for x in range(1, n + 1):
        i = [str(i) for i in range(1, x + 1)]
        u = [str(i) for i in range(x - 1, 0, -1)]
        s.append("".join(i + u))
    return "\n".join(s)


def triangle_palindromic2(n):
    return (reduce(operator.add, [f"{i}" for i in list(range(1, int(n) + 1)) + list(range(int(n) - 1, 0, -1))]))


expected = "1\n121\n12321\n1234321\n123454321"
result = triangle_palindromic(5)
assert expected == result

# assert 123454321 == triangle_palindromic2(5)

print(triangle_palindromic2(5))
