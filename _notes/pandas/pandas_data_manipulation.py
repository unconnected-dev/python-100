import pandas

#Data Manipulation
if True:
    
    #Reading from a CSV file
    csv_relative_file_path = "./_notes/pandas/file_data/read_from/random_data.csv"
    with open(csv_relative_file_path) as csv_file:
        csv_data = pandas.read_csv(csv_file)
        
    #csv_file has 4 columns
    #name, age, salary, department
    

    #Creating new columns
    if False:
        csv_data["bonus"] = csv_data["salary"] * 0.03
        print(f"{csv_data}")

    
    #Modifying column values
    if False:
        csv_data["salary"] = csv_data["salary"] * 0.5;
        print(f"{csv_data}")


    #Renaming columns
    if True:
        csv_data.columns = ["name", "age", "salary", "dept"]
        print(f"{csv_data}")


#Dropping duplicate rows
if False:
    exampleData = {
        "customer_id": [1, 2, 3, 4, 5, 6],
        "name": ["Ella", "David", "Zachary", "Alice", "Finn", "Violet"],
        "email": ["emily@example.com", "michael@example.com", "sarah@example.com", "john@example.com", "john@example.com", "alice@example.com"]
    }

    #customer_id, name, email
    exampleDataFrame = pandas.DataFrame(exampleData)
    
    #keep, will keep the first occurence
    #inplace, will modify the selected DataFrame rather than returning a new copy 
    exampleDataFrame.drop_duplicates(subset=["email"], keep="first", inplace=True)

    print(f"{exampleDataFrame}")


#Dropping rows with missing data
if False:
    exampleData = {
        "student_id": [355, 951, 470, 977, 300],
        "name": [None, None, "Quincy", "Sophia", "Liam"],
        "age": [9, 8, 20, None, 15]
    }
     
    exampleDataFrame = pandas.DataFrame(exampleData)
    #if you use .dropna() with no subset the row will be dropped if any 
    #of its columns has missing data
    
    #In this example name and age columns have missing data 
    #Specify the columns to check for missing values
    exampleDataFrame = exampleDataFrame.dropna(subset='name')

    print(f"{exampleDataFrame}")