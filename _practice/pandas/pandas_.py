
import pandas


employee_data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom', 'Emily', 'Michael', 'Sophia', 'David', 'Jessica'],
    'Age': [35, 28, 40, 45, 30, 33, 38, 29, 42, 31],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'HR'],
    'Salary': [50000, 60000, 80000, 70000, 55000, 75000, 48000, 72000, 62000, 53000]
}
employee_data_frame = pandas.DataFrame(employee_data)


student_data = {
    'StudentID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'Math': [85, 90, 75, 80, 95, 70, 85, 60, 75, 88],
    'Science': [70, 80, 65, 75, 85, 60, 75, 50, 65, 78],
    'English': [80, 85, 40, 75, 90, 65, 70, 55, 80, 82]
}
student_data_frame = pandas.DataFrame(student_data)


product_data = {
    'ProductID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Keyboard', 'Monitor', 'Printer', 'Mouse', 'Speaker', 'External Hard Drive'],
    'Stock': [50, 49, 80, 120, 150, 30, 25, 100, 75, 60],
    'Price': [1200, 800, 500, 100, 50, 300, 200, 20, 150, 80]
}
product_data_frame = pandas.DataFrame(product_data)


customer_data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom', 'Emily', 'Michael', 'Sophia', 'David', 'Jessica'],
    'Age': [35, 28, 40, 45, 30, 33, 38, 29, 42, 31],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston', 'Seattle', 'Miami', 'Denver', 'Austin', 'Atlanta']
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

#Average score for each student
if False:
    student_data_frame['Average'] = student_data_frame[['English', 'Math', 'Science']].mean(axis=1)
    print(f"{student_data_frame[['Name','Average']]}")

#Failed a subjeect < 50
if False:
    print(f"{student_data_frame[(student_data_frame['English'] < 50)\
                               | (student_data_frame['Math'] < 50)\
                                | (student_data_frame['Science'] < 50)].shape[0]}")

#Total value of the inventory for each product
if False:
    product_data_frame['TotalValue'] = product_data_frame['Stock'] * product_data_frame['Price']
    print(f"{product_data_frame[['Product','TotalValue']]}")

#Average price of products with stock above 100
if False:
    avg_data_Frame = product_data_frame[product_data_frame['Stock'] > 100]['Price'].mean()
    print(f"{avg_data_Frame}")

#How many products have a price below 100
if False:
    print(f"{product_data_frame[product_data_frame['Price'] < 100].shape[0]}")

#Most expensive product
if False:
    print(f"{product_data_frame[product_data_frame['Price'] == product_data_frame['Price'].max()]}")

#Average age of customers
if False:
    print(f'{customer_data_frame['Age'].mean()}')

#How many customers are there from each age group 20-30, 30-40 etc
if False:
    bins = [20,30,40,50,60,70]
    labels=['20-29','30-39','40-49','50-59','60-69']
    print(f"{pandas.cut(customer_data_frame['Age'], bins=bins, labels=labels).value_counts()}")

#Which city has the highest average age of customers
if False:
    print(f"{customer_data_frame.groupby('City')['Age'].mean().idxmax()}")

#How many customers have names starting with 'a'
if False:
    print(f"{customer_data_frame[customer_data_frame['Name'].str.startswith('A')].shape[0]}")

#How many employees are older than 40
if False:
    print(f"{employee_data_frame[employee_data_frame['Age'] > 40].shape[0]}")

#Who is the employee with the highest salary
if False:
    #This example generates a series
    print(f"{employee_data_frame[employee_data_frame['Salary'] == employee_data_frame['Salary'].max()]['Name']}")
    
    #To put an extra column in you need [] around the words like the example below
    #This example generates a data frame
    # print(f"{employee_data_frame[employee_data_frame['Salary'] == employee_data_frame['Salary'].max()][['Name','Age']]}")

#What is the highest grade in each subject
if False:
    print(f"{student_data_frame[['Math', 'Science', 'English']].max()}")

#Who scored the lowest in science
if False:
    print(f"{student_data_frame[student_data_frame['Science'] == student_data_frame['Science'].min()]['Name']}")

#How many products have a stock level below 50
if False:
    print(f"{product_data_frame[product_data_frame['Stock'] < 50].shape[0]}")

#Total value of the inventory
if False:
    print(f"{(product_data_frame['Stock'] * product_data_frame['Price']).sum()}")

if False:
    product_data_frame['TotalValue'] = product_data_frame['Stock'] * product_data_frame['Price']
    print(f"{product_data_frame['TotalValue'].sum()}")

#How many customers have ages between 25 and 55
if False:
    print(f"{customer_data_frame[(customer_data_frame['Age'] >= 25) | (customer_data_frame['Age'] <= 55)].shape[0]}")

#Which city has the highest number of customers
if False:
    print(f"{customer_data_frame['City'].value_counts().idxmax()}")

#How many employees names start with J
if False:
    print(f"{employee_data_frame[employee_data_frame['Name'].str.startswith('J')].shape[0]}")

#Which product has the highest total value
if False:
    product_data_frame['TotalValue'] = product_data_frame['Price'] * product_data_frame['Stock']
    print(f"{product_data_frame[product_data_frame['TotalValue'] == product_data_frame['TotalValue'].max()]['Product']}")

#How many customers are from cities starting with N
if False:
    print(f"{customer_data_frame[customer_data_frame['City'].str.startswith('N')].shape[0]}")