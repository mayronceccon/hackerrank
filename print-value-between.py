# https://www.hackerrank.com/challenges/python-print/problem


def print_value_between(n):
    return int("".join(str(x) for x in range(n + 1)))


assert 123 == print_value_between(3)
