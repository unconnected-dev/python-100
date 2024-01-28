#Lambda Functions
#Anonymous functions

#Add
if False:
    add = lambda x, y: x + y
    num1 = 2
    num2 = 3
    print(f"{num1} + {num2}: {add(num1, num2)}")

#Even numbers
if False:
    is_even = lambda x: x % 2 == 0
    for i in range(6):
        print(f"{i}: {is_even(i)}")

#Key function for sorting
if False:
    names = ["Alice", "Bob", "Charlie"]
    # sorted_names = sorted(names, key=lambda x: len(x))
    x_length = lambda x: len(x)
    sorted_names = sorted(names, key = x_length)
    print(f"{sorted_names}")

#Filtering
if False:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    is_even = lambda x: x % 2 == 0
    even_numbers = list(filter(is_even, numbers))
    print(f"{even_numbers}") 

#Maps
if False:
    numbers = [1, 2, 3, 4, 5]
    # squared_numbers = list(map(lambda x: x**2, numbers))
    map_func = lambda x: x**2
    squared_numbers = list(map(map_func, numbers))
    print(f"{squared_numbers}") 

#Combine with list comprehensions
if False:
    numbers = [1, 2, 3, 4, 5]
    # squared_evens = [x**2 for x in numbers if lambda x: x % 2 == 0]
    check_func = lambda x: x % 2 == 0
    squared_evens = [x**2 for x in numbers if check_func]
    print(f"{squared_evens}")