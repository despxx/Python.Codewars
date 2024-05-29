# 8 kyu
# Return Negative

# In this simple assignment you are given a number and have to make it negative. But maybe the
# number is already negative?

# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative(number):
    if number > 0:
        return number * (-1)
    else:
        return number

# Оптимальное решение
# def make_negative( number ):
#     return -abs(number)
