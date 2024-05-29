"""
7kyu
Shortest Word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    list_s = s.split()

    result = len(s)
    for el in list_s:
        if len(el) <= result:
            result = len(el)

    return result

"""
Optimal

def find_short(s):
    return min(len(x) for x in s.split())
"""
