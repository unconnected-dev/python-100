import pandas


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


relative_path_name = "./026_comprehensions/natoAlphabet/nato_phonetic_alphabet.csv"
with open(relative_path_name) as nato_data_file:
    nato_data = pandas.read_csv(nato_data_file)

    #To break down the pandas data frame rows
    nato_dict = {row.letter : row.code for(index, row) in nato_data.iterrows()}
    # print(nato_dict)

for student_name in ["Angela1", "James", "Lily"]:
    student_name_list = list(student_name)

    student_code = []
    try:
        for c in student_name_list:
            nato_dict[c.capitalize()]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        for c in student_name_list:
            student_code.append(nato_dict[c.capitalize()])

        print(student_code)


#DONE - - - - - - - - - - - 
    

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


