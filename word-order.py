# https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter


def word_order(data):
    d = data.split("\n")
    del d[0]
    amount_words = len(list(Counter(d)))
    counter_words = Counter(d)
    words_sum = " ".join([str(counter_words[n]) for n in counter_words])
    return "%s\n%s" % (amount_words, words_sum)


input_data = "4\nbcdef\nabcdefg\nbcde\nbcdef"
expected = "3\n2 1 1"
assert expected == word_order(input_data)


input_data = "5\nmayron\nceccon\nthomas\nlisie\nceccon"
expected = "4\n1 2 1 1"
assert expected == word_order(input_data)
