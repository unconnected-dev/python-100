import random

#List Comprehension
#Below is not list comprehension
if False:
    numbers = [1, 2, 3]
    new_list = []
    for n in numbers:
        add_1 = n + 1
        new_list.append(add_1)

    print(new_list)#[2, 3, 4]


#Below is list comprehension
#Single line version of above
if False:
    numbers = [1, 2, 3]
    new_list = [n + 1 for n in numbers]
    print(new_list)


if False:
    name = "paul"
    new_list = [letter for letter in name]
    print(new_list)#This would be the same as list()

#List, range, string, tuple are Python Sequences
#They have a specific order


#Range
if False:
    new_list = [n * 2 for n in range(1, 6)]
    print(new_list)


#Conditional List Comprehension
if False:
    names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
    new_list = [name.capitalize() for name in names if len(name) <= 4]
    print(new_list)


#Dictionary Comprehension
if False:
    # new_dict = {new_key:new_value for item in list}
    # new_dict = {new_key:new_value for (key, value) in dict.items()}

    names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
    names_dict = {name: random.randint(0, 100) for name in names}
    # print(names_dict)

    passed_students = {name: value for (name, value) in  names_dict.items() if value >= 60}
    print(passed_students)


