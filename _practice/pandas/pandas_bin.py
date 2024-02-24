
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
    'Stock': [50, 49, 80, 120, 150, 30, 25, 100, 75, 0],
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