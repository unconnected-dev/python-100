#Pandas
#Is a Python library that provides high-performance easy to use data structures and data
#analysis tools for manipulating and analyzing data

#The key components of Pandas are in its two primary data structures

#Series: A one-dimensional labeled array capable of holding any data type
#similar to a list

#DataFrame: A two-dimensional labeled data structure made of rows and columns
#similar to a spreadsheet


#Do not name the notes file pandas.py
import pandas

#Basics 
if True:
    
    #Reading from a CSV file
    csv_relative_file_path = "./_notes/pandas/file_data/read_from/random_data.csv"
    with open(csv_relative_file_path) as csv_file:
        csv_data = pandas.read_csv(csv_file)

    #csv_file has 4 columns
    #name, age, salary, department
    if False:
        print(f"{csv_data}")


    #Iterating through rows of a DataFrame
    if False:
        for (index, row) in csv_data.iterrows():
            print(f"{row}")


    #Selecting a column (series)
    if False:
        print(f"{csv_data['name']}")
        print(f"{csv_data.name}")

    
    #Selecting rows
    if False:
        print(f"{csv_data[csv_data.department == 'IT']}")
        print(f"{csv_data[csv_data.salary >= 70000]}")


    #Convert to dict
    #The conversion groups by columns
    #col1:{
    #       row1:
    #       row2:
    #    },
    #col2:{
    #       row1:
    #       row2:
    #   }
    if False:
        csv_data_dict = csv_data.to_dict()
        print(f"{csv_data_dict}")
    

    #Converting to a regular dict
    #Using dictionary comprehension and iterrows a more normal dictionary
    #can be created
    if False:
        csv_dict = {row['name']: row['salary'] for (index, row) in csv_data.iterrows()}
        print(f"{csv_dict}")


    #Convert column (series) to list
    if False:
        csv_data_list = csv_data.name.to_list()
        print(f"{csv_data_list}")

    
    #In built Pandas functions
    if False:
        average_salary = csv_data.salary.mean()
        highest_salary = csv_data.salary.max()
        print(f"average: {average_salary}, highest: {highest_salary}")


if False:
    #Creating a dict from selected data from DataFrame
    csv_relative_file_path = "./_notes/pandas/file_data/read_from/squirrel_data.csv"
    with open(csv_relative_file_path) as csv_file:
        squir_data = pandas.read_csv(csv_file)

    gray_squirrel_count = len(squir_data[squir_data["Primary Fur Color"] == "Gray"])
    cinnamon_squirrel_count = len(squir_data[squir_data["Primary Fur Color"] == "Cinnamon"])
    black_squirrel_count = len(squir_data[squir_data["Primary Fur Color"] == "Black"])


    squir_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
    }

    #Creating a new DataFrame from a dict
    squir_count_data = pandas.DataFrame(squir_dict)
    print(f"{squir_count_data}")