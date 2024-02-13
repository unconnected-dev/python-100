#Unpacking
#This is the process of extracting individual elements from an
#iterable (such as a list, tuple, or dictionary) and assigning
#them to separate variables in a single statement

#Tuple unpacking
if False:
    x, y, z = (1, 2, 3)
    print(f"x: {x}")

#List unpacking
if False:
    [a, b, c] = [1, 2, 3]
    print(f"{a}")

#Extended iterable unpacking
if False:
    a, *b = [1, 2, 3, 4, 5]
    print(f"{b}")

#Dictionary unpacking
if False:
    d = {'a':1, 'b':2, 'c':3}
    x, y, z = d.values()
    print(f"z: {z}")

#Unpacking in function calls
if False:
    def add(a, b, c):
        return a + b + c
    
    values = [1, 2, 3]
    print(add(*values))

#Unpacking in list comprehensions
if False:
    numbers = [(1, 2), (3, 4), (5, 6)]
    flattened = [x for sublist in numbers for x in sublist]
    print(f"{flattened}")

#Unpacking with `zip`
if False:
    names = ['alice', 'bob', 'charlie']
    ages = [30, 25, 35]
    for name, age in zip(names, ages):
        print(f"name: {name}, age: {age}")