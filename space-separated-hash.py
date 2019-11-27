# https://www.hackerrank.com/challenges/python-tuples/problem


def hash_space(n, l):
    return hash(tuple(l))


assert 3713081631934410656 == hash_space(2, [1, 2])
