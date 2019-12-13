# https://www.hackerrank.com/challenges/find-angle/problem

import math


def find_angle_mbc(a, b):
    x3 = math.pow((math.pow(a, 2) + math.pow(b, 2)), (1 / 2))
    angle = round(math.asin(a / x3) * 180 / math.pi)
    return "%d°" % (round(angle))


assert '45°' == find_angle_mbc(10, 10)
assert '6°' == find_angle_mbc(1, 10)
