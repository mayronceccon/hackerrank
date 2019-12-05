# https://www.hackerrank.com/challenges/python-time-delta/problem

import datetime


def time_delta(t1, t2):
    t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    diff = t1 - t2
    seconds = diff.total_seconds()
    return abs(int(seconds))


t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'
assert 25200 == time_delta(t1, t2)

t1 = 'Sat 02 May 2015 19:54:36 +0530'
t2 = 'Fri 01 May 2015 13:54:36 -0000'
assert 88200 == time_delta(t1, t2)


t1 = 'Fri 11 Feb 2078 00:05:21 +0400'
t2 = 'Mon 29 Dec 2064 03:33:48 -1100'
assert 413962293 == time_delta(t1, t2)

t1 = 'Wed 29 Aug 2029 06:11:15 +0900'
t2 = 'Thu 11 Sep 2217 22:45:23 +0630'
assert 5933847848 == time_delta(t1, t2)
