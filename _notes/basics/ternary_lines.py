#Ternary Lines
#value_if_true if condition else value_if_false

#Even or odd
if False:
    for num in range(0, 16):
        result = "Even" if num % 2 == 0 else "Odd"
        print(f"{num} : {result}")

#Positive, negative or zero
if False:
    for num in range(-5, 6):
        result = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
        print(f"{num} : {result}")

#Absolute value
if False:
    num = -7
    absolute_value = num if num >= 0 else -num
    print(f"{num} : {absolute_value}")

#List to string
if False:
    my_list = [42, 37, 18]
    result = ", ".join(map(str, my_list)) if my_list else "No elements"
    print(f"{result}")

#Leap year
if False:
    year = 2024
    is_leap_year = "Leap year" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "Not a leap year"
    print(f"{year} : {is_leap_year}")

#Grades
if False:
    numeric_grade = 85
    letter_grade = "A" if numeric_grade >= 90 else "B" if numeric_grade >= 80 else "C" if numeric_grade >= 70 else "D" if numeric_grade >= 60 else "F"
    print(f"{numeric_grade} : {letter_grade}")

#Dictionary sign categorization
if True:
    num = 1
    sign_category = {1: "Positive", -1: "Negative"}[num // abs(num)] if num != 0 else "Zero"
    print(f"{num} : {sign_category}")