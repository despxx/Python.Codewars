"""
7kyu
Exes and Ohs

Check to see if a string has the same amount of 'x's and 'o's. The method must return a
boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):
    list_s = list(s.lower())
    if list_s.count("o") != list_s.count("x"):
        return False
    else:
        return True

"""
Optimal

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
"""
