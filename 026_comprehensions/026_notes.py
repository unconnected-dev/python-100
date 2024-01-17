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
if True:
    names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
    new_list = [name.capitalize() for name in names if len(name) <= 4]
    print(new_list)