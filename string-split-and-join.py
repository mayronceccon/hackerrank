# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    return "-".join(line.split(" "))


assert "mayron-thomas-ceccon" == split_and_join("mayron thomas ceccon")
