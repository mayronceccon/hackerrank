# https://www.hackerrank.com/challenges/python-lists/problem

from io import StringIO
from unittest.mock import patch


def commands_for_list(data):
    commands = data.strip().split('\n')[1:]
    list_of_data = []
    for command in commands:
        data = command.split()
        cmd = data[0]

        if cmd == 'insert':
            k = int(data[1])
            v = int(data[2])
            list_of_data.insert(k, v)

        if cmd == 'remove':
            v = int(data[1])
            list_of_data.remove(v)

        if cmd == 'append':
            v = int(data[1])
            list_of_data.append(v)

        if cmd == 'sort':
            list_of_data.sort()

        if cmd == 'pop':
            list_of_data.pop()

        if cmd == 'reverse':
            list_of_data.reverse()

        if cmd == 'print':
            print(list_of_data)


data = """
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""

with patch('sys.stdout', new=StringIO()) as fakeOutput:
    commands_for_list(data)
assert "[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]" == fakeOutput.getvalue().strip()

data = """
29
append 1
append 6
append 10
append 8
append 9
append 2
append 12
append 7
append 3
append 5
insert 8 66
insert 1 30
insert 6 75
insert 4 44
insert 9 67
insert 2 44
insert 9 21
insert 8 87
insert 1 75
insert 1 48
print
reverse
print
sort
print
append 2
append 5
remove 2
print
"""

result = """
[1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
[5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
[1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
[1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]
"""

with patch('sys.stdout', new=StringIO()) as fakeOutput:
    commands_for_list(data)

assert result.strip() == fakeOutput.getvalue().strip()
