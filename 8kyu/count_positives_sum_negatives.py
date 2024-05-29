"""
8kyu
Count of positives / sum of negatives

Given an array of integers.
Return an array, where the first element is the count of positives numbers and the second
element is sum of negative numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should
return [10, -65].
"""

def count_positives_sum_negatives(arr):

    if arr:
        count_positive = 0
        summ_negatives = 0

        for i in arr:
            if i > 0:
                count_positive += 1
            elif i <= 0:
                summ_negatives += i

        return [count_positive, summ_negatives] if count_positive or \
        summ_negatives != 0 else [0, 0]
    else:
        return []

print(count_positives_sum_negatives([0,0]))

"""
Optimal

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]
"""
