#Squaring Numbers
if False:
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [n * n for n in numbers]

    print(squared_numbers)

#Filter Even Numbers
if True:
    s = "9, 0, 32, 8, 2, 64, 29, 42, 99"
    list_of_strings = s.split(",")

    filtered_numbers = [int(n) for n in list_of_strings if int(n) % 2 == 0]
    print(filtered_numbers)