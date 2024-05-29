"""
8kyu
You only need one - Beginner

You will be given an array a and a value x. All you need to do is check whether the provided
array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
"""

def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    else:
        return False

"""
Optimal

def check(seq, elem):
    return elem in seq
"""
