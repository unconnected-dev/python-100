
import pandas


employee_data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'Age': [35, 28, 40, 45, 30],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT'],
    'Salary': [50000, 60000, 80000, 70000, 55000]
}
employee_data_frame = pandas.DataFrame(employee_data)


student_data = {
    'StudentID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Math': [85, 90, 75, 80, 95],
    'Science': [70, 80, 65, 75, 85],
    'English': [80, 85, 70, 75, 90]
}
student_data_frame = pandas.DataFrame(student_data)


product_data = {
    'ProductID': [1, 2, 3, 4, 5],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Keyboard'],
    'Stock': [50, 100, 80, 120, 150],
    'Price': [1200, 800, 500, 100, 50]
}
product_data_frame = pandas.DataFrame(product_data)


customer_data = {
    'CustomerID': [101, 102, 103, 104, 105],
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'Age': [35, 28, 40, 45, 30],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
}
customer_data_frame = pandas.DataFrame(customer_data)


#Iterating through rows
if False:
    for (index, row) in customer_data_frame.iterrows():
        print(f"{row}")

#Iterating through rows and seleting column
if False:
    for (index, row) in customer_data_frame.iterrows():
        print(f"{row['Name']}")

#Average age of employees
if False:
    print(f"{employee_data_frame['Age'].mean()}")

#How many employees in IT department
if False:
    print(f"{employee_data_frame[employee_data_frame['Department'] == 'IT'].shape}")

#Employees that earn more than 60,000
if False:
    print(f"{employee_data_frame[employee_data_frame['Salary'] > 60000]['Name']}")

#What is the average grade in each subject
if False:
    print(f"{student_data_frame[['English', 'Science', 'Math']].mean()}")

#Highest score in english
if False:
    max_english_score = student_data_frame['English'].max()
    print(f"{student_data_frame[student_data_frame['English'] == max_english_score]['Name']}")

#Find students who pass all subjects, >=70
if False:
    print(f"{student_data_frame[(student_data_frame['English'] >= 70)\
                                 & (student_data_frame['Math'] >= 70)\
                                & (student_data_frame['Science'] >= 70)]}")

#Total potential revenue
if False:
    total = 0
    for (index, row) in product_data_frame[['Stock','Price']].iterrows():
        total += row['Stock'] * row['Price']
    
    print(f"Total: {total}")

if False:
    product_data_frame['TotalRevenue'] = product_data_frame['Price'] * product_data_frame['Stock']
    print(f"{product_data_frame['TotalRevenue'].sum()}")

#List product stock below 100
if False:
    print(f"{product_data_frame[product_data_frame["Stock"] < 100]}")

#How many customers from each city
if False:
    print(f"{customer_data_frame['City'].value_counts()}")

#Average age of customers in each city
if False:
    print(f"{customer_data_frame.groupby('City')['Age'].mean()}")

#List names of customers under 30
if False:
    print(f"{customer_data_frame[customer_data_frame['Age'] < 30]['Name']}")

#How many employees are there in each department
if False:
    print(f"{employee_data_frame['Department'].value_counts()}")

#What is the average salary in each department
if False:
    print(f"{employee_data_frame.groupby('Department')['Salary'].mean()}")

#Who is the youngest employee
if False:
    print(f"{employee_data_frame[employee_data_frame['Age'] == employee_data_frame['Age'].min()]}")

#What is the total salary expense for the company
if False:
    print(f"{employee_data_frame['Salary'].sum()}")

#How many students scored above 80 in all subjects
if False:
    print(f"{student_data_frame[(student_data_frame['English'] >= 80)\
                                & (student_data_frame['Math'] >= 80)\
                                & (student_data_frame['Science'] >= 80)].shape[0]}")

#Highest overall
if False:
    #axis=1 performs the operation along the rows
    student_data_frame['Total'] = student_data_frame[['English', 'Math', 'Science']].sum(axis=1)
    print(f"{student_data_frame[student_data_frame['Total'] == student_data_frame['Total'].max()]}")