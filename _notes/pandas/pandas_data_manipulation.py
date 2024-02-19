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
    if False:
        csv_data.columns = ["name", "age", "salary", "dept"]
        print(f"{csv_data}")


#Filling missing data
if False:
    exampleData = {
        "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
        "quantity": [None, None, 779, 849],
        "price": [135, 821, 9319, 3051]
    }

    #name, quantity, price
    exampleDataFrame = pandas.DataFrame(exampleData)

    #Filling missing data with 0
    exampleDataFrame["quantity"] = exampleDataFrame["quantity"].fillna(0)

    print(f"{exampleDataFrame}")


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


#Merging DataFrames (tables)
if True:
    exampleData_1 = {
        "student_id": [1, 2, 3, 4],
        "name": ["Mason", "Ava", "Taylor", "Georgia"],
        "age": [8, 6, 15, 17]
    }

    exampleData_2 = {
        "student_id": [5, 6],
        "name": ["Leo", "Alex"],
        "age": [7, 7]
    }
    
    #concat is used to concatenate pandas objects along a particular axis
    #with optional set logic along the other
    df1 = pandas.DataFrame(exampleData_1)
    df2 = pandas.DataFrame(exampleData_2)
    df_combined = pandas.concat([df1, df2])
    
    print(f"{df_combined}")