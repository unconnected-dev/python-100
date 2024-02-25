
import numpy
import pandas


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
    'Price': [1200, 800, 500, 100, 50, 300, 200, 20, 150, 80, 450, 30]
}
product_data_frame = pandas.DataFrame(product_data)


customer_data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom', 'Emily', 'Michael', 'Sophia', 'David', 'Jessica', 'Daniel', 'Olivia'],
    'Age': [35, 28, 40, 45, 30, 33, 38, 29, 40, 31, 36, 27],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston', 'Seattle', 'Miami', 'Denver', 'Austin', 'Atlanta', 'Detroit', 'Phoenix']
}
customer_data_frame = pandas.DataFrame(customer_data)


#Bins in pandas are used to create intervals or categories into which you can place
#your data. These intervals can be defined by specifying the start and end points as
#well as the step size


#Create age bins with intervals of 10 years each and count the number of employees in each bin
if False:
    employee_data_frame['Age_bins'] = pandas.cut(employee_data_frame['Age'], bins=range(20, 60, 10), right=False)
    age_distribution = employee_data_frame.groupby('Age_bins').size()
    print(f"Age distribution: {age_distribution}")

#Divide the student dataset into three performance catergories based on their average scores in
#Math, Science and English: Low, Medium and High
if False:
    student_data_frame['Average_score'] = (student_data_frame['English'] + student_data_frame['Math'] + student_data_frame['Science'])/3
    performance_bins = [0, 60, 80, 100]
    performance_labels = ['Low', 'Medium', 'High']
    student_data_frame['Performance'] = pandas.cut(student_data_frame['Average_score'], bins=performance_bins, labels= performance_labels)
    print(f"{student_data_frame[['Name','Performance']]}")

#Bin the product dataset based on their prices into three price ranges Low, Medium and High
if False:
    price_bins = [0, 100, 500, numpy.inf]
    price_labels = ['Low', 'Medium', 'High']
    product_data_frame['Price_range'] = pandas.cut(product_data_frame['Price'], bins=price_bins, labels=price_labels)
    print(f"{product_data_frame[['Product', 'Price_range']]}")

#Categorize the customer dataset into three age groups: Young, Middle-aged, Elderly
if False:
    age_bins = [0, 30, 50, numpy.inf]
    age_labels = ['Young', 'Middle-aged', 'Elderly']
    customer_data_frame['Age_group'] = pandas.cut(customer_data_frame['Age'], bins=age_bins, labels=age_labels)
    print(f"{customer_data_frame[['Name', 'Age_group']]}")

#Bin the stock levels of products into four categories: Low, Medium, High and Out of stock
if False:
    stock_bins = [-numpy.inf, 0, 50, 100, numpy.inf]
    stock_labels = ['Out of stock', 'Low', 'Medium', 'High']
    product_data_frame['Stock_level'] = pandas.cut(product_data_frame['Stock'], bins=stock_bins, labels=stock_labels)
    print(f"{product_data_frame[['Product', 'Stock_level']]}")

#Divide the employee dataset into two age groups: Young < 35, Old >=35
if False:
    age_bins = [0, 35, numpy.inf]
    age_labels = ['Young', 'Old']
    employee_data_frame['Age_group'] = pandas.cut(employee_data_frame['Age'], bins=age_bins, labels=age_labels)
    print(f"{employee_data_frame[['Name','Age_group']]}")

#Bin the ages of employees into five equal intervals and count the number of employees
#in each inverval
if False:
    age_bins = pandas.cut(employee_data_frame['Age'], bins=5)
    age_distribution = employee_data_frame.groupby(age_bins).size()
    print(f"{age_distribution}")

#Group the student dataset into two age groups: Under 20 and 20 and above
if False:
    age_bins = [0, 20, numpy.inf]
    age_labels = ['Under 20', '20 and above']
    student_data_frame['Age_group'] = pandas.cut(student_data_frame['Age'], bins=age_bins, labels=age_labels)
    print(f"{student_data_frame[['Name','Age_group']]}")

#Categorize the prices of products into three groups: Cheap, Moderate, Expensive
if False:
    price_bins = [0, 100, 500, numpy.inf]
    price_labels = ['Cheap','Moderate','Expensive']
    product_data_frame['Price_group'] = pandas.cut(product_data_frame['Price'], bins=price_bins, labels=price_labels)
    print(f"{product_data_frame[['Product', 'Price_group']]}")

#Bin the ages of customers into three groups: Under 30, 30-50, Over 50
if False:
    age_bins = [0, 30, 50, numpy.inf]
    age_labels = ['Under 30', '30-50', 'Over 50']
    customer_data_frame['Age_group'] = pandas.cut(customer_data_frame['Age'], bins=age_bins, labels=age_labels)
    print(f"{customer_data_frame[['Name','Age_group']]}")

#Bin the Math scores of students into three categories: Low 0-60, Medium 61-80 and High, 81-100
if False:
    math_bins = [0, 60, 80, 100]
    math_labels = ['Low', 'Medium', 'High']
    student_data_frame['Math_category'] = pandas.cut(student_data_frame['Math'], bins=math_bins, labels=math_labels)
    print(f"{student_data_frame[['Name','Math_category']]}")

#Group the ages of employees into four intervals: 20-30, 31-40, 41-50 and 51 and above
if False:
    age_bins = [20,31,41,51,numpy.inf]
    age_labels = ['20-30','31-40','41-50','51 and above']
    employee_data_frame['Age_interval'] = pandas.cut(employee_data_frame['Age'], bins=age_bins,labels=age_labels, right=False)
    print(f"{employee_data_frame[['Name','Age_interval']]}")

#Categorize the stock levels of products into Low 0-25, Medium 26-75 and High 76 and above
if False:
    stock_bins = [0,26,76,numpy.inf]
    stock_labels =['Low','Medium','High']
    product_data_frame['Stock_level'] = pandas.cut(product_data_frame['Stock'], bins=stock_bins,labels=stock_labels, right=False)
    print(f"{product_data_frame[['Product', 'Stock', 'Stock_level']]}")

#Divide the English scores of students into five groups
#Fail 0-49, Pass 50-64, Credit 65-74, Distinction 75-84, High Distinction 85-100
if False:
    score_bins = [0,50,65,75,85,100]
    score_labels = ['Fail','Pass','Credit','Distinction','High Distinction']
    student_data_frame['English_group'] = pandas.cut(student_data_frame['English'], bins=score_bins, labels=score_labels, right=False)
    print(f"{student_data_frame[['Name','English','English_group']]}")

#Bin the prices of products into Cheap 0-100, Moderate 101-300 and Expensive 301 and above
if False:
    price_bins = [0,100,300,numpy.inf]
    price_labels = ['Cheap','Moderate','Expensive']
    product_data_frame['Price_group'] = pandas.cut(product_data_frame['Price'],bins=price_bins,labels=price_labels)
    print(f"{product_data_frame[['Product','Price','Price_group']]}")

#Group the ages of customers into three intervals: under-25, 25-40, over 40
if False:
    age_bins = [0,25,40,numpy.inf]
    age_labels = ['Under 25', '25-40','Over 40']
    customer_data_frame['Age_group'] = pandas.cut(customer_data_frame['Age'],bins=age_bins,labels=age_labels)
    print(f"{customer_data_frame[['Name','Age','Age_group']]}")

#Categorize the salaries of employees into four groups: Low, Medium, High, Very High
if False:
    salary_bins = [0, 60000, 80000, 100000, numpy.inf]
    salary_labels = ['Low','Medium','High','Very High']
    employee_data_frame['Salary_group'] = pandas.cut(employee_data_frame['Salary'],bins=salary_bins,labels=salary_labels, right=False)
    print(f"{employee_data_frame[['Name','Salary','Salary_group']]}")

#Divide the Science scores of students into 
#Fail 0-49, Pass 50-64, Credit 65-74, Distinction 75-84, High Distinction 85-100
if False:
    student_bins = [0,50,65,75,85,100]
    student_labels =['Fail','Pass','Credit','Distinction','High Distinction']
    student_data_frame['Science_group'] = pandas.cut(student_data_frame['Science'],bins=student_bins,labels=student_labels,right=False)
    print(f"{student_data_frame[['Name','Science','Science_group']]}")

#Bin the ages of customers into Young 0-30, Middle-aged 31-50, Elderly 51 and above
if False:
    age_bins = [0,30,50,numpy.inf]
    age_labels = ['Young','Middle-aged','Elderly']
    customer_data_frame['Age_group'] = pandas.cut(customer_data_frame['Age'], bins=age_bins,labels=age_labels)
    print(f"{customer_data_frame[['Name','Age','Age_group']]}")

#Group the Math scores of students into
#Fail 0-49, Pass 50-64, Credit 65-74, Distinction 75-84, High Distinction 85-100
if False:
    student_bins = [0,50,65,75,85,100]
    student_labels =['Fail','Pass','Credit','Distinction','High Distinction']
    student_data_frame['Math_group'] = pandas.cut(student_data_frame['Math'],bins=student_bins,labels=student_labels,right=False)
    print(f"{student_data_frame[['Name','Math','Math_group']]}")