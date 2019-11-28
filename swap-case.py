# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(words):
    new_word = ''
    for word in words:
        if word.islower():
            new_word += word.upper()

        if word.isupper():
            new_word += word.lower()

        if not word.isupper() and not word.islower():
            new_word += word
    return new_word


expected = 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
result = swap_case('HackerRank.com presents "Pythonist 2".')

assert expected == result
