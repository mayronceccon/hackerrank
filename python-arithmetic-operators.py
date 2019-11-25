# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

def arithmetic_operators(first, second):
    lista = [
        first + second,
        first - second,
        first * second
    ]
    return "\n".join(str(n) for n in lista)

assert '5\n1\n6' == arithmetic_operators(3, 2)
assert '10\n0\n25' == arithmetic_operators(5, 5)
assert '15\n-1\n56' == arithmetic_operators(7, 8)
