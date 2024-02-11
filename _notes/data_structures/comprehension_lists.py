#Comprehension Lists
#[expression for item in iterable if condition]

#Uppercase
if False:
    words = ["apple", "banana", "berry"]
    uppercased = [word.upper() for word in words]
    print(f"{uppercased}")

#Square numbers
if False:
    squares = [(x, x**2) for x in range(10)]
    print(f"{squares}")

#Double even numbers
if False:
    evens = [(x, 2 * x) for x in range(10) if x % 2 == 0]
    print(f"{evens}")

#List of lengths
if False:
    sentence = "This is an example sentence"
    word_lengths = [len(word) for word in sentence.split()]
    print(f"{word_lengths}")

#Flatten 2d matrix
#Note: Can use multiple for
if False:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [element for row in matrix for element in row]
    print(f"{flattened}")

#Creating a list of tuples from two lists
if False:
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 22]
    persons = [(name, age) for name, age in zip(names, ages)]
    print(f"{persons}")

#Using ternary expression in list comprehension
#Note: Can put ternary expression in
if False:
    numbers = [1, 2, 3, 4, 5]
    categorized = [(x, "Even" if x % 2 == 0 else "Odd") for x in numbers]
    print(categorized)

#Creating a dictionary from two lists
if False:
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 22]
    persons = {name: age for name, age in zip(names, ages)}
    print(persons)
    