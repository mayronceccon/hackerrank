# https://www.hackerrank.com/challenges/whats-your-name/problem


def print_full_name(first_name, last_name):
    return f"Hello {first_name} {last_name}! You just delved into python."


expected = "Hello Ross Taylor! You just delved into python."
result = print_full_name("Ross", "Taylor")

assert expected == result
