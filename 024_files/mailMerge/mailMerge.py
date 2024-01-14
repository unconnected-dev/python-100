#Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

NAME_TAG = "[name]"

relative_file_path_invited = "./024_files/mailMerge/Input/Names/invited_names.txt"
relative_file_path_letter = "./024_files/mailMerge/Input/Letters/starting_letter.txt"
relative_file_path_target_directory = "./024_files/mailMerge/Output/ReadyToSend/"

with open(relative_file_path_invited) as invited_names_file:
    names = invited_names_file.readlines()

with open(relative_file_path_letter) as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        name = name.strip()
        new_letter_contents = letter_contents.replace(NAME_TAG, name)
    
    
        with open(f"{relative_file_path_target_directory}/{name}.txt", "w") as write_file:
            write_file.write(new_letter_contents)