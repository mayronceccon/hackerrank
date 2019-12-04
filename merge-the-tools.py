# https://www.hackerrank.com/challenges/merge-the-tools/problem

from io import StringIO
from unittest.mock import patch


def merge_the_tools(string, k):
    if k == 1:
        print("\n".join(string))
        return

    sequences = [string[n:n + k] for n in range(0, k*k, k)]
    for sequence in sequences:
        seq = ''
        for letter in sequence:
            if letter not in seq:
                seq += letter
        print(seq)


with patch('sys.stdout', new=StringIO()) as fakeOutput:
    merge_the_tools("AABCAAADA", 3)
assert "AB\nCA\nAD" == fakeOutput.getvalue().strip()


f = "A" * 1000
with patch('sys.stdout', new=StringIO()) as fakeOutput:
    merge_the_tools(f, 1)
assert "\n".join(f) == fakeOutput.getvalue().strip()
