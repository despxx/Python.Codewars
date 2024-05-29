"""
8kyu
Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.

For example:
[1, 2, 3] --> [2, 4, 6]
"""

def maps(a):
    return [i * 2 for i in a]

print(maps([1, 2, 3]))

# Алтернативное решение
# def maps(a):
#     return map(lambda x:2*x, a)
