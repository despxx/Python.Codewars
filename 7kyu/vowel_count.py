"""
7kyu
Vowel Count

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    count = 0
    for i in sentence:
        if i in "aeoiuAEOIU":
            count += 1

    return count

"""
Optimal

def getCount(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")
"""
