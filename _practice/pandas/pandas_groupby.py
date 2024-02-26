import pandas
import numpy

employee_data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom', 'Emily', 'Michael', 'Sophia', 'David', 'Jessica', 'Daniel', 'Olivia', 'Ethan'],
    'Age': [35, 28, 40, 45, 30, 33, 38, 29, 42, 31, 36, 27, 41],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [50000, 60000, 80000, 70000, 55000, 75000, 48000, 72000, 62000, 53000, 78000, 59000, 68000]
}
employee_data_frame = pandas.DataFrame(employee_data)


student_data = {
    'StudentID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack', 'Kate', 'Liam', 'Mia'],
    'Math': [85, 90, 75, 80, 95, 70, 85, 60, 75, 88, 82, 93, 78],
    'Science': [70, 80, 65, 75, 85, 60, 75, 50, 65, 78, 72, 83, 68],
    'English': [80, 85, 40, 75, 90, 65, 70, 55, 80, 82, 75, 88, 72],
    'Age': [19, 21, 22, 20, 21, 18, 20, 21, 22, 20, 19, 21, 22]
}
student_data_frame = pandas.DataFrame(student_data)


product_data = {
    'ProductID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Keyboard', 'Monitor', 'Printer', 'Mouse', 'Speaker', 'External Hard Drive', 'Camera', 'USB Drive'],
    'Stock': [50, 49, 80, 120, 150, 30, 25, 100, 75, 0, 65, 40],
    'Price': [1200, 800, 500, 100, 50, 300, 200, 20, 150, 80, 450, 30],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Office Supplies', 'Office Supplies', 'Electronics', 'Electronics', 'Photography', 'Office Supplies']
}
product_data_frame = pandas.DataFrame(product_data)


customer_data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom', 'Emily', 'Michael', 'Sophia', 'David', 'Jessica', 'Daniel', 'Olivia'],
    'Age': [35, 28, 40, 45, 30, 33, 38, 29, 40, 31, 36, 27],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston', 'Seattle', 'Miami', 'Denver', 'Austin', 'Atlanta', 'Detroit', 'Phoenix']
}
customer_data_frame = pandas.DataFrame(customer_data)


#What is the average salary for each department
if False:
    average_department_salary = employee_data_frame.groupby('Department')['Salary'].mean()
    print(f"{average_department_salary}")

#How many students belong to each age group
#18-20, 21-23, etc
if False:
    bins = [17, 20, 23, 26]
    labels = ['18-20', '21-23', '24-26']

    student_data_frame['Age_group'] = pandas.cut(student_data_frame['Age'],bins=bins,labels=labels)
    students_by_age_group = student_data_frame.groupby('Age_group').size()
    print(f"{students_by_age_group}")

    number_of_students = student_data_frame.groupby('Age')

#What is the total stock and revenue (stock * price) for each product category
if False:
    product_data_frame['Revenue'] = product_data_frame['Stock'] * product_data_frame['Price']

    total_stock_revenue_by_category = product_data_frame.groupby('Category').agg({'Stock': 'sum', 'Revenue': 'sum'})
    print(total_stock_revenue_by_category)

#What is the average grade in each subject for each age group?
if False:
    bins = [17, 20, 23, 26]
    labels = ['18-20', '21-23', '24-26']

    student_data_frame['AgeGroup'] =  pandas.cut(student_data_frame['Age'],bins=bins,labels=labels)
    average_grades = student_data_frame.groupby(['AgeGroup']).agg({'Math': 'mean', 'Science': 'mean', 'English': 'mean'})
    print(f"{average_grades}")

#How many customers are there in each city for each age group?
if False:
    age_bins = [20,31,41,51,numpy.inf]
    age_labels = ['20-30','31-40','41-50','51 and above']
    customer_data_frame['AgeGroup'] = pandas.cut(customer_data_frame['Age'],bins=age_bins,labels=age_labels)

    totals = customer_data_frame.groupby(['City','AgeGroup']).size()
    print(f"{totals}")

#Average salary of employees in each department
if False:
    avg_salary = employee_data_frame.groupby('Department')['Salary'].mean()
    print(f"{avg_salary}")

#How many students are there in each age group
if False:
    age_group_count = student_data_frame.groupby('Age').size()
    print(f"{age_group_count}")

#What is the total stock and average price of products in each category
if False:
    category_summary = product_data_frame.groupby('Category').agg({'Stock': 'sum', 'Price': 'mean'})
    print(f"{category_summary}")

#What is the maximum age of customers in each city
if False:
    age_high = customer_data_frame.groupby(['City'])['Age'].max()
    print(f"{age_high}")

#How many products are out of stock in each category
if False:
    out_of_stock = product_data_frame.loc[product_data_frame['Stock'] == 0].groupby('Category').size()
    print(f"{out_of_stock}")

#What is the median age of employees in each department group
if False:
    median_ages = employee_data_frame.groupby('Department').agg({'Age': 'median'})
    print(f"{median_ages}")

#How many employees are in each age group 20s,30s,40s
if False:
    age_bin =[20, 30, 40, 50, numpy.inf]
    age_labels = ['20s','30s','40s','50s and over']

    employee_data_frame['Age_group'] = pandas.cut(employee_data_frame['Age'],bins=age_bin,labels=age_labels,right=False)
    print(f"{employee_data_frame.groupby('Age_group').size()}")

#What is the minimum and maximum price of products in each category?
if False:
    print(f"{product_data_frame.groupby('Category').agg({'Price': ['min','max']})}")

#How many customers are there from each city in each age group 20s, 30s, 40s
if False:
    age_bin =[20, 30, 40, 50, numpy.inf]
    age_labels = ['20s','30s','40s','50s and over']

    customer_data_frame['Age_group'] = pandas.cut(customer_data_frame['Age'], bins=age_bin, labels=age_labels)
    print(f"{customer_data_frame.groupby(['City','Age_group']).size()}")

#What is the average stock level of products in each category, considering only products
#with stock greater than 0
if False:
    above_zero = product_data_frame.loc[product_data_frame['Stock'] > 0]
    print(f"{above_zero.groupby('Category').agg({'Stock':'mean'})}")

if False:
    stock_avg_by_category = product_data_frame[product_data_frame['Stock'] > 0].groupby('Category')['Stock'].mean()
    print(f"{stock_avg_by_category}")

#What is the average salary in each department
if False:
    print(f"{employee_data_frame.groupby('Department')['Salary'].mean()}")

#How many employees are there in each department
if False:
    print(f"{employee_data_frame.groupby('Department').size()}")

#What is the maximum age of students in each age group
if False:
    bins = [18, 20, 22]
    labels = ['18-20', '21-22']

    student_data_frame['Age_group'] = pandas.cut(student_data_frame['Age'],bins=bins, labels=labels)
    print(f"{student_data_frame.groupby('Age_group')['Age'].max()}")

#What is the total stock and average price of products in each category?
if False:
    print(f"{product_data_frame.groupby('Category').agg({'Stock':'sum','Price':'mean'})}")

#How many customers are there in each city and what is the average age of customers in each city?
if False:
    print(f"{customer_data_frame.groupby('City').agg({'CustomerID':'size', 'Age':'mean'})}")

#What is the total salary expense and average age of employees in each department?
if False:
    print(f"{employee_data_frame.groupby('Department').agg({'Salary':'sum','Age':'mean'})}")

#What is the highest and lowest price of products in each category?
if False:
    print(f"{product_data_frame.groupby('Category').agg({'Price':['max','min']})}")

#What is the total stock and average price of products per category in the electronics category only
if False:
    electronics = product_data_frame.loc[product_data_frame['Category'] == 'Electronics']
    electronics_stats = electronics.groupby('Category').agg({'Stock': 'sum', 'Price': 'mean'})
    print(f"{electronics_stats}")

#What is the average age of employees in each age group
if False:
    bins = [20, 30, 40, 50, 60, 70]
    labels = ['20s', '30s', '40s', '50s', '60s+']
    employee_data_frame['Age_group'] = pandas.cut(employee_data_frame['Age'],bins=bins,labels=labels)

    print(f"{employee_data_frame.groupby('Age_group')['Age'].mean()}")

#How many products are there in each category and what is the average price
if False:
    print(f"{product_data_frame.groupby('Category').agg({'Price':'mean','Stock':'sum'})}")

#What is the total stock of products and the average price, consider only stock > 0
if False:
    above_zero = product_data_frame[product_data_frame['Stock'] > 0]
    print(f"{above_zero.groupby('Category').agg({'Stock':'sum','Price':'mean'})}")

#What is the total score and average score of each student across all subjects
if False:
    student_data_frame['Total_score'] = student_data_frame['English'] + student_data_frame['Math'] + student_data_frame['Science']
    student_data_frame['Average_score'] = student_data_frame['Total_score'] / 3
    print(f"{student_data_frame[['Name','Total_score','Average_score']]}")

if False:
    student_data_frame['Total_score'] = student_data_frame[['Math','English','Science']].sum(axis=1)
    student_data_frame['Average_score'] = student_data_frame['Total_score'] / 3
    print(f"{student_data_frame}")

#What is the total salary expense and average age of employees in each age group
#from the HR department
if False:
    hr_dept = employee_data_frame[employee_data_frame['Department'] == 'HR']
    bins = [20, 30, 40, 50, 60, 70]
    labels = ['20s', '30s', '40s', '50s', '60s+']
    hr_dept['Age_group'] = pandas.cut(hr_dept['Age'],bins=bins,labels=labels)

    print(f"{hr_dept.groupby('Age_group').agg({'Salary':'sum','Age':'mean'})}")