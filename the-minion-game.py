# https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string):
    VOWELS = "AEIOU"

    length = len(string)
    stuart = 0
    kevin = 0
    for position in range(length):
        if string[position] not in VOWELS:
            stuart += length - position
        else:
            kevin += length - position

    if stuart == kevin:
        return "Draw"
    elif stuart > kevin:
        return f"Stuart {stuart}"
    else:
        return f"Kevin {kevin}"


assert "Stuart 12" == minion_game("BANANA")
assert "Stuart 300300" == minion_game("NANAN" * 200)
