import string
import math

# Binary Addition

def add_binary(a, b):
    summ = a + b

    output = ""
    while summ > 0:
        output += str(summ % 2)
        summ //= 2

    return output[::-1]

#---------------------------------------------------

# Categorize New Member

def open_or_senior(data):
    output = []
    for member in data:
        if member[0] >= 55 and member[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")

    return output

#---------------------------------------------------

# Complementary DNA

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

#---------------------------------------------------

# Credit Card Mask

def maskify(cc):
    output = "#" * (len(cc) - 4) + cc[-4:]

    return output

#---------------------------------------------------

# Descending Order

def descending_order(num):
    list_str = list(str(num))
    list_int = [int(i) for i in list_str]
    list_int.sort(reverse=True)
    result = int("".join(map(str, list_int)))

    return result

#---------------------------------------------------

# Disemvowel Trolls

def disemvowel(string_):
    for let in string_:
        if let in "aeoiuAEOIU":
            string_ = string_.replace(let, "")

    return string_

#---------------------------------------------------

# Exes and Ohs

def xo(s):
    list_s = list(s.lower())
    if list_s.count("o") != list_s.count("x"):
        return False
    else:
        return True

#---------------------------------------------------

# Find the divisors!

def divisors(integer):
    output = []
    for i in range(2, integer):
        if integer % i == 0:
            output.append(i)

    return output if output != [] else str(integer) + " is prime"

#---------------------------------------------------

# Find the next perfect square!

def find_next_square(sq):
    if sq % math.sqrt(sq) == 0:
        return (math.sqrt(sq) + 1) ** 2
    else:
        return -1

#---------------------------------------------------

# Friend or Foe?

def friend(x):
    outputArr = []
    for i in x:
        if len(i) == 4:
            outputArr.append(i)

    return outputArr

#---------------------------------------------------

# Get the Middle Character

def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1] + s[len(s) // 2]
    elif len(s) == 1:
        return s
    else:
        return s[len(s) // 2]

#---------------------------------------------------

# Growth of a Population

def nb_year(p0, percent, aug, p):

    summYears = 0
    while p0 < p:
        summYears += 1
        p0 = math.floor(p0 + (p0 * percent / 100) + aug)

    return summYears

#---------------------------------------------------

# Highest and Lowest

def high_and_low(numbers):
    numbers_list = numbers.split(" ")

    int_list = []
    for i in numbers_list:
        int_list.append(int(i))

    max_num = str(max(int_list))
    min_el = str(min(int_list))

    return f"{max_num} {min_el}"

#---------------------------------------------------

# Isograms

def is_isogram(string):

    string = string.lower()
    set_ = set(string)

    if len(set_) == len(string):
        return True
    else:
        return False

#---------------------------------------------------

# Is this a triangle?

def is_triangle(a, b, c):
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        return True if a * b * c > 0 else False
    else:
        return False

#---------------------------------------------------

# Jaden Casing Strings

def to_jaden_case(string):

    result_str = " ".join(word[0].upper() + word[1:].lower() for word in string.split())

    return result_str

#---------------------------------------------------

# List Filtering

def filter_list(l):

    result = []
    for i in l:
        if type(i) == int:
            result.append(i)

    return result

#---------------------------------------------------

# Mumbling

def accum(st):

    st_low = st.lower()
    list_st = []
    count = 0
    for i in st_low:
        list_st.append(i.upper() + i * count)
        count += 1
    res_str = "-".join(list_st)

    return res_str

#---------------------------------------------------

# Number of People in the Bus

def number(bus_stops):

    summ0 = 0
    summ1 = 0
    for i in bus_stops:
        summ0 += i[0]
        summ1 += i[1]

    return summ0 - summ1

#---------------------------------------------------

# Odd or Even?

def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

#---------------------------------------------------

# Ones and Zeros

def binary_array_to_number(arr):
    str_ = ""
    for i in arr:
        str_ += str(i)

    return int(str_, 2)

#---------------------------------------------------

# Printer Errors

def printer_error(s):
    count = 0
    for i in s.lower():
        if i in "nopqrstuvwxyz":
            count += 1

    return f"{count}/{len(s)}"

#---------------------------------------------------

# Regex validate PIN code

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

#---------------------------------------------------

# Remove the minimum

def remove_smallest(numbers):
    if len(numbers) < 2:
        return []
    else:
        output = numbers.copy()
        output.remove(min(numbers))
        return output

#---------------------------------------------------

# Reverse words

def reverse_words(text):
    arrText = text.split(" ")

    outputArr = []
    for word in arrText:
        outputArr.append(word[::-1])

    output = " ".join(outputArr)

    return output

#---------------------------------------------------

# Shortest Word

def find_short(s):
    list_s = s.split()

    result = len(s)
    for el in list_s:
        if len(el) <= result:
            result = len(el)

    return result

#---------------------------------------------------

# Square Every Digit

def square_digits(num):
    str_num = str(num)
    arr = [int(i) ** 2 for i in str_num]
    str_arr = [str(x) for x in arr]
    str_ = "".join(str_arr)

    return int(str_)

#---------------------------------------------------

# String ends with?

def solution(text, ending):
    if text[((len(text)) - (len(ending))):] == ending:
        return True
    else:
        return False

#---------------------------------------------------

# Sum of the first nth term of Series

def series_sum(n):

    summ = 0
    divider = 1
    for i in range(n):
        summ += 1 / divider
        divider += 3

    return format(summ, ".2f")

#---------------------------------------------------

# Sum of odd numbers

def row_sum_odd_numbers(n):
    return n ** 3

#---------------------------------------------------

# Beginner Series #3 Sum of Numbers

def get_sum(a, b):
    if a < b:
        return sum([i for i in range(a, b + 1)])
    else:
        return sum([i for i in range(b, a + 1)])

#---------------------------------------------------

# Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    summ = min(numbers)
    numbers.remove(min(numbers))
    summ += min(numbers)

    return summ

#---------------------------------------------------

# Two to One

def longest(a1, a2):
    array1 = set(a1)
    array2 = set(a2)
    newArr = array1 | array2
    outputArr = list(newArr)
    outputArr.sort()
    output = "".join(outputArr)

    return output

#---------------------------------------------------

# Vowel Count

def get_count(sentence):
    count = 0
    for i in sentence:
        if i in "aeoiuAEOIU":
            count += 1

    return count

#---------------------------------------------------

# You're a square!

def is_square(n):
    if n < 0:
        return False
    elif math.sqrt(n) % 0.5 == 0:
        return True
    else:
        return False
