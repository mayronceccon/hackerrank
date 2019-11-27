# https://www.hackerrank.com/challenges/finding-the-percentage/problem

def finding_the_percentage(index, data, name):
    marks = [float(mark) for mark in data[name]]
    average = sum(marks) / len(marks)
    return format(average, '.2f')


data = {'Krishna': [67, 68, 69], 'Arjun': ['70', '98', '63'], 'Malika': ['52', 56, '60']}
assert format(56.00, '.2f') == finding_the_percentage(3, data, 'Malika')
