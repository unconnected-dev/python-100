path_name = "C:/_GitHub/python-100/024_files/a_text_file.txt"

#Basic File
if False:
    a_file = open(path_name)
    a_file_contents = a_file.read()
    a_file.close()
    print(a_file_contents)

#This will close after use
if False:
    with open(path_name) as another_file:
        file_contents = another_file.read()
        print(file_contents)

#Write to file
if True:
    #"w" is write, will also create the file if it doesn't exist
    #"a" is append
    with open(path_name, "w") as write_file:
        write_file.write("replacement text")