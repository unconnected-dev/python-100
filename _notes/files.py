#Files

#File paths can be absolute or relative
absolute_path_name = "C:/_GitHub/python-100/_notes/file_data/data.txt"
relative_path_name = "./_notes/file_data/data.txt"


#Opening file
#mode: 'r' is used for reading
if False:
    def openAndPrintContents(file_path):
        with open(file_path, "r") as a_file:
            file_contents = a_file.read()
            return file_contents

    print(f"{openAndPrintContents(relative_path_name)}")


#Reading line by line
if False:
    def readingLines(file_path):
        with open(file_path, "r") as a_file:
            #readlines() returns a list
            lines = a_file.readlines()
            
            rl = []
            for line in lines:
                rl.append(line.strip().split(' ')[0])
        
        return rl
    
    print(f"{readingLines(relative_path_name)}")


#Writing to a file
#mode 'w' is used for writing
#This will also create the file if it does not exist
#mode 'a' is used to append
if False:
    def writeToFile(file_path):
        with open(file_path, 'w') as write_file:
            for i in range(10):
                write_file.write(f'{i}\n')

        with open(file_path, 'r') as read_file:
            contents = read_file.read()
    
        return contents
    
    create_relative_path_name = "./_notes/file_data/write_file.txt"
    print(f"{writeToFile(create_relative_path_name)}")