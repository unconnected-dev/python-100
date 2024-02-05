#Dictionaries
#An unordered collcetion of key-value pairs

#Dicionary basics
if False:
    # a_dict = dict()     #either = dict() or = {} can create a dictionary
    # b_dict = {}
    
    c_dict = {
        1: 'a',
        2: 'b',
        3: 'c',
    }

    #Adding or modifying to dictionary
    c_dict[4] = 'd'

    def iterate_over(dict_):
        #Accessing elements
        for key, val in c_dict.items():
            print(f"key: {key}, val: {val}")

    iterate_over(c_dict)

    #Removing elements
    del c_dict[3]
    c_dict.pop(4)

    iterate_over(c_dict)

    #Clear all items
    c_dict.clear()

#Iteration
if False:
    i_dict = {}
    for i in range(5):
        i_dict[i] = f"{i}..."

    #Over keys
    if False:
        for key in i_dict:
            print(f"{i_dict[key]}")
    
    #Over values
    if False:
        for val in i_dict.values():
            print(f"{val}")
    
    if True:
        for key, val in i_dict.items():
            print(f"key: {key}, val: {val}")

#Default values
if False:
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    #Using get() with a default value
    value_a = my_dict.get('a', 'Key not found')
    value_d = my_dict.get('d', 'Key not found')

    print(value_a)  #Output: 1
    print(value_d)  #Output: Key not found

#Merging dictionaries
if False:
    a_dict = {
        0: 'a',
        2: 'c',
        3: 'd',
    }

    b_dict = {
        1: 'b'
    }

    a_dict.update(b_dict)
    for key, val in a_dict.items():
        print(f"key: {key}, val: {val}")

#Shallow copy dictionaries
if False:
    #Shallow copy creates a new object but not copies of the nested objects within
    import copy

    original_list = [1, [2, 3], 4]
    shallow_copy = copy.copy(original_list)

    shallow_copy[1][0] = 'X'

    #Both the original and copied structures are affected
    print("Original List:", original_list)   #Output: [1, ['X', 3], 4]
    print("Shallow Copy:", shallow_copy)     #Output: [1, ['X', 3], 4]

#Deep copy dictionaries
if False:
    #Deep copy creates a new object and recursively creates copies of all objects found in the original
    import copy

    original_list = [1, [2, 3], 4]
    deep_copy = copy.deepcopy(original_list)

    deep_copy[1][0] = 'Y'

    #The original structure remains unaffected
    print("Original List:", original_list)   #Output: [1, [2, 3], 4]
    print("Deep Copy:", deep_copy)           #Output: [1, ['Y', 3], 4]

#Unpacking
if False:
    #Use the ** operator to unpack key-value pairs and pass as keyword arguments
    def display_info(name, age, city):
        print(f'Name: {name}, Age: {age}, City: {city}')

    my_dict = {'name': 'Alice', 'age': 30, 'city': 'London'}

    display_info(**my_dict)

if False:
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    a, b, c = my_dict.values()
    print(f'a: {a}, b: {b}, c: {c}')