# https://www.hackerrank.com/challenges/nested-list/problem

from operator import itemgetter


def nested_list_student(students):
    list_students = sorted(students, key=itemgetter(1))
    list_students_without_first = filter(lambda x: x[1] > list_students[0][1], list_students)
    list_students_without_first = list(list_students_without_first)
    list_students_second = filter(lambda x: x[1] == list_students_without_first[0][1], list_students_without_first)
    data = [s[0] for s in sorted(list_students_second, key=itemgetter(0))]
    return "\n".join(data)


students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
assert 'Berry\nHarry' == nested_list_student(students)

students = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
assert 'Beria\nHarsh' == nested_list_student(students)
