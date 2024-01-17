#Squaring Numbers
if False:
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [n * n for n in numbers]

    print(squared_numbers)

#Filter Even Numbers
if False:
    s = "9, 0, 32, 8, 2, 64, 29, 42, 99"
    list_of_strings = s.split(",")

    filtered_numbers = [int(n) for n in list_of_strings if int(n) % 2 == 0]
    print(filtered_numbers)

#Check common numbers
if False:
    relative_file_1_path = "./026_comprehensions/file_1.txt"
    relative_file_2_path = "./026_comprehensions/file_2.txt"

    with open(relative_file_1_path) as file_1:
        file_1_numbers = file_1.readlines()#Generates a list
        file_1_numbers = [s.strip() for s in file_1_numbers]

    with open(relative_file_2_path) as file_2:
        file_2_numbers = file_2.readlines()#Generates a list
        file_2_numbers = [s.strip() for s in file_2_numbers]

    # for n in file_1_numbers:
    #     if n in file_2_numbers:
    #         print(n)

    results = [int(n) for n in file_1_numbers if n in file_2_numbers]
    print(results)

#Dictionary comprehension
if True:
    sentence = "What is the air speed velocity"
    sentence_list = sentence.split()
    
    sentence_dict = {word: len(word) for word in sentence_list}
    print(sentence_dict)
    