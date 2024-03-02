import pandas

employees_data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'employee_name': ['John', 'Jane', 'Alice', 'Bob', 'Michael', 'Emily', 'David', 'Sophia'],
    'department_id': [101, 102, 101, 103, 102, 103, 101, 104]
}
employees_data_frame = pandas.DataFrame(employees_data)

departments_data = {
    'department_id': [101, 102, 103, 104, 105],
    'department_name': ['HR', 'Finance', 'IT', 'Marketing', 'Operations']
}
department_data_frame = pandas.DataFrame(departments_data)

salary_data = {
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'salary': [60000, 70000, 55000, 80000, 75000, 60000, 65000, 70000]
}
salary_data_frame = pandas.DataFrame(salary_data)

location_data = {
    'department_id': [101, 102, 103, 104, 105],
    'location': ['New York', 'Chicago', 'San Francisco', 'Los Angeles', 'Seattle']
}
location_data_frame = pandas.DataFrame(location_data)




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