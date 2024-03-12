import os

absolute_path_name = "C:/_GitHub/python-100/024_files/a_text_file.txt"
relative_path_name = "./024_files/a_text_file.txt"

# print(os.getcwd())

#Basic File
if False:
    a_file = open(absolute_path_name)
    a_file_contents = a_file.read()
    a_file.close()
    print(a_file_contents)

#This will close after use
if True:
    with open(relative_path_name) as another_file:
        file_contents = another_file.read()
        print(file_contents)

#Write to file
if False:
    #"w" is write, will also create the file if it doesn't exist
    #"a" is append
    with open(absolute_path_name, "w") as write_file:
        write_file.write("replacement text")