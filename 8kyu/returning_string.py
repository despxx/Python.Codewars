"""
8kyu
Returning Strings

Make a function that will return a greeting statement that uses an input; your program
should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
"""

def greet(name):
    return "Hello, {0} how are you doing today?".format(name)

# Другой вариант

# def greet(name):
#     return f'Hello, {name} how are you doing today?'
