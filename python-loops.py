# https://www.hackerrank.com/challenges/python-loops/problem


def loops(n):
    lista = [a**2 for a in range(n)]
    return "\n".join(str(x) for x in lista)


assert "0\n1\n4\n9\n16" == loops(5)
