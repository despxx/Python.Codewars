"""
7kyu
Highest and Lowest

RIn this little assignment you are given a string of space separated numbers, and have
to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 32 4 -5") # return "32 -5"

Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""

def high_and_low(numbers):
    numbers_list = numbers.split(" ")

    int_list = []
    for i in numbers_list:
        int_list.append(int(i))

    max_num = str(max(int_list))
    min_el = str(min(int_list))

    return f"{max_num} {min_el}"

"""
Optimal

def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"
"""
