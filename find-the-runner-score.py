# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def find_the_runner_score(n, arr):
    l = list(dict.fromkeys(arr))
    l.sort(reverse=True)
    return int(l[1])


assert 2 == find_the_runner_score(2, '2 9'.split())
assert 5 == find_the_runner_score(5, '2 3 6 6 5'.split())
assert 8 == find_the_runner_score(8, '2 3 6 6 5 9 8 4 7'.split())
