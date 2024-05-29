"""
8kyu
Fake Binary

Given a random non-negative number, you have to return the digits of this number within an
array in reverse order.
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and
above with '1'. Return the resulting string.

Note: input will never be an empty string
"""

def fake_bin(x):

    result = ""

    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"

    return result

"""
Optimal

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
"""
