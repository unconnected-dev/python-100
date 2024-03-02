import pandas
import numpy

employees_data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'employee_name': ['John', 'Jane', 'Alice', 'Bob', 'Michael', 'Emily', 'David', 'Sophia', 'Emma', 'William'],
    'department_id': [101, 102, 101, 103, 102, 103, 101, 104, 105, 105],
    'joining_date': ['2020-01-15', '2019-05-20', '2021-02-10', '2022-03-08', '2020-11-25', None, None, None, '2023-03-20', '2022-07-10']
}
employees_data_frame = pandas.DataFrame(employees_data)

departments_data = {
    'department_id': [101, 102, 103, 104, 105, 106],
    'department_name': ['HR', 'Finance', 'IT', 'Marketing', 'Operations', 'Legal'],
    'manager_id': [1, 2, 4, 5, 7, 9],
    'office_phone': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123', '567-890-1234', None]
}
department_data_frame = pandas.DataFrame(departments_data)

salary_data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'salary': [60000, 70000, 55000, 80000, 75000, 60000, 65000, 70000, 85000, 90000],
    'bonus': [5000, 6000, numpy.nan, numpy.nan, numpy.nan, 5000, 5500, 6000, 7500, 8000]
}
salary_data_frame = pandas.DataFrame(salary_data)

location_data = {
    'department_id': [101, 102, 103, 104, 105, 106],
    'location': ['New York', 'Chicago', 'San Francisco', 'Los Angeles', 'Seattle', 'Boston'],
    'floor': [12, 8, 20, 15, 10, 5]
}
location_data_frame = pandas.DataFrame(location_data)

manager_data = {
    'manager_id': [1, 2, 4, 5, 7, 9],
    'manager_name': ['John', 'Jane', 'Bob', 'Michael', 'David', 'Emma']
}
manager_data_frame = pandas.DataFrame(manager_data)




#How many employees are in each department
if False:
    merged_ = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    print(f"{merged_.groupby('department_name')['employee_id'].count()}")

#What are the names of employees who work in HR
if False:
    merged_ = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    print(f"{merged_.loc[merged_['department_name'] == 'HR']['employee_name'].tolist()}")

#What are the departments where no employees are assigned
if False:
    merged_ = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    empty_ = department_data_frame[~department_data_frame['department_id'].isin(merged_['department_id'])]
    print(f"{empty_}")

#What is the average salary in each department
if False:
    merged_salary = pandas.merge(employees_data_frame, salary_data_frame, on='employee_id', how='left')
    merged_salary_department = pandas.merge(merged_salary, department_data_frame, on='department_id', how='left')
    print(f"{merged_salary_department.groupby('department_name')['salary'].mean()}")

#What is the total salary expense for each department
if False:
    merged_salary = pandas.merge(employees_data_frame, salary_data_frame)
    merged_salary_department = pandas.merge(merged_salary, department_data_frame, on='department_id', how='left')
    print(f"{merged_salary_department.groupby('department_name')['salary'].sum()}")

#How many employees are there in each location
if False:
    merged_department = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    merged_department_location = pandas.merge(merged_department, location_data_frame, on='department_id', how='left')
    print(f"{merged_department_location.groupby('location')['employee_id'].count()}")

#What is the average salary of employees in each location
if False:
    merged_department = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    merged_department_salary = pandas.merge(merged_department, salary_data_frame, on='employee_id', how='left')
    merged_department_salary_location = pandas.merge(merged_department_salary, location_data_frame, on='department_id', how='left')
    print(f"{merged_department_salary_location.groupby('location')['salary'].mean()}")

#Who are the names of employees at each location
if False:
    merged_department = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    merged_department_location = pandas.merge(merged_department, location_data_frame, on='department_id', how='left')
    print(f"{merged_department_location.groupby('location')['employee_name'].apply(list)}")

if False:
    merged_department = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    merged_department_location = pandas.merge(merged_department, location_data_frame, on='department_id', how='left')
    grouped_by_location = merged_department_location.groupby('location')['employee_name'].apply(list)

    for location, employees in grouped_by_location.items():
        print(f"{location}...")
        for employee in employees:
            print(f"{employee}")
        
        print(f"")

#Merge the employees data with salary
if False:
    merged_ = pandas.merge(employees_data_frame, salary_data_frame, on='employee_id', how='left')
    print(f"{merged_}")

#Merge employee data with department
if False:
    merged_ = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    print(f"{merged_}")

#Merge employee data with location
if False:
    merged_ = pandas.merge(employees_data_frame, location_data_frame, on='department_id', how='left')
    print(f"{merged_}")

#Combine all dataframes into one
if False:
    employee_department = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='left')
    employee_department_salary = pandas.merge(employee_department, salary_data_frame, on='employee_id', how='left')
    employee_department_salary_location = pandas.merge(employee_department_salary, location_data_frame, on='department_id', how='left')
    print(f"{employee_department_salary_location}")

if False:
    merged_all = employees_data_frame.merge(salary_data_frame, on='employee_id').merge(department_data_frame, on='department_id').merge(location_data_frame, on='department_id')
    print(f"{merged_all}")

#Join employee and departments, then fill missing values with unknown
if False:
    merged_ = employees_data_frame.merge(department_data_frame, on='department_id').fillna('Unknown')
    print(f"{merged_}")