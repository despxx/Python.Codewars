"""
8kyu
Century From Year

including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28
"""

def century(year):
    return int((year + 99) / 100)

print(century(1601))

"""
Optimal

def century(year):
    return (year + 99) // 100
"""
