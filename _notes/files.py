#Files

#File paths can be absolute or relative
absolute_path_name = "C:/_GitHub/python-100/_notes/file_data/read_from/data.txt"
relative_path_name = "./_notes/file_data/read_from/data.txt"


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
    
    write_to_relative_path_name = "./_notes/file_data/write_to/write_file.txt"
    print(f"{writeToFile(write_to_relative_path_name)}")


#Replacing tags in a template file with csv file data
if False:
    NAME_TAG = "[name]"
    PRODUCT_TAG = "[product]"
    ORDER_NUMBER_TAG = "[order_number]"
    COMPANY_NAME_TAG = "[company_name]"

    def generateLetters(template_file_path, template_data_file_path, write_to_file_path):
        with open(template_data_file_path, 'r') as template_data_file:
            entries = template_data_file.readlines()
            entries = entries[1:]

        with open(template_file_path) as template_file:
            template_contents = template_file.read()

            for entry in entries:
                entry_list = entry.split(',')
                name = entry_list[0].strip()
                product = entry_list[1].strip()
                order_number = entry_list[2].strip()
                company_name = entry_list[3].strip()
    
                letter_contents = template_contents.replace(NAME_TAG, name)\
                                                .replace(PRODUCT_TAG, product)\
                                                .replace(ORDER_NUMBER_TAG, order_number)\
                                                .replace(COMPANY_NAME_TAG, company_name)
                
                with open(f"{write_to_file_path}/{name.lower()}_{product.lower()}.txt", 'w') as write_file:
                    write_file.write(letter_contents)


    template_relative_file_path = "./_notes/file_data/read_from/template.txt"
    template_data_relative_file_path = "./_notes/file_data/read_from/template_data.csv"
    write_to_relative_path_name = "./_notes/file_data/write_to"
    generateLetters(template_relative_file_path, template_data_relative_file_path, write_to_relative_path_name)


if False:
    import pandas

    NAME_TAG = "[name]"
    PRODUCT_TAG = "[product]"
    ORDER_NUMBER_TAG = "[order_number]"
    COMPANY_NAME_TAG = "[company_name]"

    def generateLetters(template_file_path, template_data_file_path, write_to_file_path):
        with open(template_data_file_path, 'r') as template_data_file:
            entries_data = pandas.read_csv(template_data_file)
            print(entries_data)

        with open(template_file_path, 'r') as template_file:
            template_contents = template_file.read()

            for index, row in entries_data.iterrows():
                name = row['name'].strip()
                product = row['product'].strip()
                order_number = row['order_number']
                company_name = row['company_name'].strip()
    
                letter_contents = template_contents.replace(NAME_TAG, name)\
                                                .replace(PRODUCT_TAG, product)\
                                                .replace(ORDER_NUMBER_TAG, str(order_number))\
                                                .replace(COMPANY_NAME_TAG, company_name)
                
                with open(f"{write_to_file_path}/{name.lower()}_{product.lower()}.txt", 'w') as write_file:
                    write_file.write(letter_contents)


    template_relative_file_path = "./_notes/file_data/read_from/template.txt"
    template_data_relative_file_path = "./_notes/file_data/read_from/template_data.csv"
    write_to_relative_path_name = "./_notes/file_data/write_to"
    generateLetters(template_relative_file_path, template_data_relative_file_path, write_to_relative_path_name)