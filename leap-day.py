# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(y):
    if (y % 400 == 0):
        return True
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False

assert True == is_leap(2000)
assert True == is_leap(2400)
assert False == is_leap(1800)
assert False == is_leap(1900)
assert False == is_leap(1990)
assert False == is_leap(2100)
assert False == is_leap(2200)
assert False == is_leap(2300)
assert False == is_leap(2500)
