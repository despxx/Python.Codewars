# A Needle in the Haystack

def find_needle(haystack):
    return f"found the needle at position {haystack.index("needle")}"

#---------------------------------------------------

# Abbreviate a Two Word Name

def abbrev_name(name):
    return name.upper().split()[0][0] + "." + name.upper().split()[1][0]

#---------------------------------------------------

# Are You Playing Banjo?

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].upper() == "R" else f"{name} does not play banjo"

#---------------------------------------------------

# Basic Mathematical Operations

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return "Неверный математический оператор"

#---------------------------------------------------

# Calculate average

def find_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) != 0 else 0

#---------------------------------------------------

# Calculate BMI

def bmi(weight, height):

    bmi = weight / height ** 2

    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

#---------------------------------------------------

# Century From Year

def century(year):
    return int((year + 99) / 100)

#---------------------------------------------------

# Beginner Series #2 Clock

def past(h, m, s):
    if h > 23 or m > 59 or s > 59:
        return "Error input"
    else:
        return h * 3600000 + m * 60000 + s * 1000

#---------------------------------------------------

# Convert a Boolean to a String

def boolean_to_string(b):
    return "True" if b == True else "False"

#---------------------------------------------------

# Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"

#---------------------------------------------------

# Convert number to reversed array of digits

def digitize(n):
    return [int(x) for x in str(n)[::-1]]

#---------------------------------------------------

# Convert a Number to a String!

def number_to_string(num):
    return str(num)

#---------------------------------------------------

# Convert a String to a Number!

def string_to_number(s):
    return int(s)

#---------------------------------------------------

# Count by X

def count_by(x, n):
    arr = [i * x for i in range(1, n + 1)]
    return arr

#---------------------------------------------------

# Count of positives / sum of negatives

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

#---------------------------------------------------

# If you can't sleep, just count sheep!!

def count_sheep(n):
    answer = ""
    for i in range(1, n + 1):
        answer += str(i) + " sheep..."

    return answer

#---------------------------------------------------

# Counting sheep...

def count_sheeps(sheep):

    count_sheeps = 0
    for i in sheep:
        if i == True:
            count_sheeps += 1

    return count_sheeps

#---------------------------------------------------

# DNA to RNA Conversion

def dna_to_rna(dna):
    list_dna = list(dna)
    list_rna = []
    for i in list_dna:
        if i == "T":
            i = "U"
            list_rna.append(i)
        else:
            list_rna.append(i)

    str_rna = "".join(list_rna)

    return str_rna

#---------------------------------------------------

# You Can't Code Under Pressure #1

def double_integer(i):
    return i * 2

#---------------------------------------------------

# Even and Odds

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#---------------------------------------------------

# Fake Binary

def fake_bin(x):

    result = ""

    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"

    return result

#---------------------------------------------------

# Find the smallest integer in the array

def find_smallest_int(arr):

    small_int = arr[0]
    for i in arr:
        if i < small_int:
            small_int = i

    return small_int

#---------------------------------------------------

# Function 1 - hello world

def greet():
    text = "hello world!"
    return text

#---------------------------------------------------

# Grasshopper - Summation

def summation(num):
    summ = 0
    while num != 0:
        summ += num
        num -= 1

    return summ

#---------------------------------------------------

# How good are you really?

def better_than_average(class_points, you_points):
    return True if you_points > sum(class_points) / len(class_points) else False

#---------------------------------------------------

# Invert values

def invert(lst):
    return [-i for i in lst]

#---------------------------------------------------

# Is he gonna survive?

def hero(bullets, dragons):
    if bullets / dragons >= 2:
        return True
    else:
        return False

#---------------------------------------------------

# Is n divisible by x and y?

def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    return False

#---------------------------------------------------

# Keep Hydrated!

def litres(time):
    return time // 2

#---------------------------------------------------

# Beginner - Lost Without a Map

def maps(a):
    return [i * 2 for i in a]

#---------------------------------------------------

# MakeUpperCase

def make_upper_case(s):
    return s.upper()

#---------------------------------------------------

# Multiply the numbers

def multiply(n):

    str_n = str(n)
    if n >= 0:
        res = n * 5 ** len(str_n)
    else:
        res = n * 5 ** (len(str_n) - 1)

    return res

#---------------------------------------------------

# Multiply

def multiply(a, b):
    return a * b

#---------------------------------------------------

# Opposite number

def opposite(number):
    return -number

#---------------------------------------------------

# Opposites Attract

def lovefunc(flower1, flower2):
    if (flower1 + flower2) % 2 == 0:
        return False
    return True

#---------------------------------------------------

# Beginner - Reduce but Grow

def grow(arr):
    mult = 1
    for i in arr:
        mult *= i

    return mult

#---------------------------------------------------

# Remove First and Last Character

def remove_char(s):
    return s[1:len(s)-1]

#---------------------------------------------------

# Remove String Spaces

def no_space(x):
    return x.replace(" ", "")

#---------------------------------------------------

# Return Negative

def make_negative(number):
    if number > 0:
        return number * (-1)
    else:
        return number

#---------------------------------------------------

# Returning Strings

def greet(name):
    return "Hello, {0} how are you doing today?".format(name)

#---------------------------------------------------

# Reversed sequence

def reverse_seq(n):
    arr = list(range(n, 0, -1))
    return arr

#---------------------------------------------------

# Reversed Strings

def solution(string):
    string = string[::-1]
    return string

#---------------------------------------------------

# Rock Paper Scissors!

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock") or \
        (p1 == "rock" and p2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

#---------------------------------------------------

# Beginner Series #1 School Paperwork

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

#---------------------------------------------------

# Sentence Smash

def smash(words):

    str_res = " ".join(words)

    return str_res

#---------------------------------------------------

# Simple multiplication

def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

#---------------------------------------------------

# Square(n) Sum

def square_sum(numbers):

    summ = 0
    for num in numbers:
        squ = num * num
        summ += squ

    return summ

#---------------------------------------------------

# String repeat

def repeat_str(repeat, string):
    return repeat * string

#---------------------------------------------------

# Sum Arrays

def sum_array(a):
    summ = 0
    for i in a:
        summ += i
    return summ

#---------------------------------------------------

# Sum of positive

def positive_sum(arr):

    summ = 0
    for num in arr:
        if num > 0:
            summ += num

    return summ

#---------------------------------------------------

# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False

#---------------------------------------------------

# You only need one - Beginner

def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    else:
        return False

#---------------------------------------------------
