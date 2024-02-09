#Comprehension Dictionaries
#{key_expression: value_expression for item in iterable}

#Square numbers
if False:
    squares_dict = {num: num**2 for num in range(10)}
    print(f"{squares_dict}")

#Double even numbers
if False:
    evens_dict = {n: n**n for n in range(10) if n % 2 ==0}
    print(f"{evens_dict}")

#Word frequency counting
if False:
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_freq_dict = {word: words.count(word) for word in words}
    print(f"{word_freq_dict}")

#Swapping keys and values
if False:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    swapped_dict = {val: key for key, val in my_dict.items()}
    print(f"{swapped_dict}")

#Filtering dictionary items
if False:
    ages = {'John': 25, 'Alice': 30, 'Bob': 22, 'Eve': 35}
    adults = {key: val for key, val in ages.items() if val >= 18}
    print(f"{adults}")

#Creating a dictionary from two lists
if False:
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    combined_dict = {key: val for key, val in zip(keys, values)}
    print(f"{combined_dict}")