
# https://www.hackerrank.com/challenges/python-division/problem


def python_division(a, b):
    lista = [
        a // b,
        a / b
    ]
    return "\n".join(str(n) for n in lista)


assert '1\n1.3333333333333333' == python_division(4, 3)
