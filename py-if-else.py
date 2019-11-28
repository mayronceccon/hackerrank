# https://www.hackerrank.com/challenges/py-if-else/problem


def python_if_else(n):
    if n % 2 == 0 and n > 20:
        return 'Not Weird'

    if n % 2 == 1:
        return 'Weird'

    if n % 2 == 0 and n in range(2, 5 + 1):
        return 'Not Weird'

    if n % 2 == 0 and n in range(6, 20 + 1):
        return 'Weird'


assert 'Not Weird' == python_if_else(50)
assert 'Weird' == python_if_else(3)
assert 'Weird' == python_if_else(5)
assert 'Weird' == python_if_else(15)
assert 'Weird' == python_if_else(7)
assert 'Not Weird' == python_if_else(2)
assert 'Weird' == python_if_else(10)
assert 'Weird' == python_if_else(20)
assert 'Not Weird' == python_if_else(24)
assert 'Not Weird' == python_if_else(100)
