"""
7kyu
Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement
a function that determines whether a string that contains only letters is an isogram. Assume
the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
"""

def is_isogram(string):

    string = string.lower()
    set_ = set(string)

    if len(set_) == len(string):
        return True
    else:
        return False

print(is_isogram("moOse"))

"""
Optimal

def is_isogram(string):
    return len(string) == len(set(string.lower()))
"""
