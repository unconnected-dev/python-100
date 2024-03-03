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

#Merge employee, salary then filter employees with salary > 70000
if False:
    merged_ = employees_data_frame.merge(salary_data_frame, on='employee_id')
    print(f"{merged_.loc[merged_['salary'] > 70000]}")

#Merge employees, departments using outer join
if False:
    merged_ = employees_data_frame.merge(department_data_frame, on='department_id', how='outer')
    print(f"{merged_}")

#Merge employees, departments and locations, then count the number of employees in each location
if False:
    merged_ = employees_data_frame.merge(department_data_frame, on='department_id').merge(location_data_frame, on='department_id')
    print(f"{merged_.groupby('location')['employee_id'].count()}")

#Combine employees, departments using inner join
if False:
    merged_ = pandas.merge(employees_data_frame, department_data_frame, on='department_id', how='inner')
    print(f"{merged_}")

#Merge employees and salary, then concatenate with location data frame
#Concat does not match up the department_id, it just sticks the columns on to the side
if False:
    merged_ = pandas.merge(employees_data_frame, salary_data_frame, on='employee_id', how='left')
    concatenated_ = pandas.concat([merged_, location_data_frame], axis=1)
    print(f"{concatenated_}")

#Calculate total salary, salary + bonus for each employee
if False:
    merged_ = employees_data_frame.merge(salary_data_frame, on='employee_id')
    merged_['total_salary'] = merged_['salary'] + merged_['bonus'].fillna(0)
    print(f"{merged_[['employee_name','total_salary']]}")

#Average salary for each department
if False:
    merged_ = employees_data_frame.merge(salary_data_frame, on='employee_id')
    merged_['total_salary'] = merged_['salary'] + merged_['bonus'].fillna(0)
    merged_ = merged_.merge(department_data_frame, on='department_id', how='left')
    print(f"{merged_.groupby('department_name')['total_salary'].mean()}")

#Find the number of employees in each location
if False:
    merged_ = employees_data_frame.merge(location_data_frame, on='department_id')
    print(f"{merged_.groupby('location')['employee_name'].count()}")

#Calculate the total bonus of employees in each department
if False:
    merged_ = employees_data_frame.merge(department_data_frame, on='department_id').merge(salary_data_frame, on='employee_id')
    result_sorted = merged_.groupby('department_name')['bonus'].sum().sort_values(ascending=False)
    print(f"{result_sorted}")

#Get managers name for each employee
if False:
    merged_ = employees_data_frame.merge(department_data_frame, on='department_id').merge(manager_data_frame, on='manager_id')
    print(f"{merged_[['employee_name','manager_name']]}")

#Find the average salary of employees in each location
if False:
    merged_ = employees_data_frame.merge(salary_data_frame, on='employee_id').merge(location_data_frame, on='department_id')
    result_ = merged_.groupby('location')['salary'].mean().sort_values(ascending=False)
    print(f"{result_}")

#Calculate the total salary + bonus for employees in each department
if False:
    merged_ = employees_data_frame.merge(salary_data_frame, on='employee_id').merge(department_data_frame, on='department_id')
    merged_['total_salary'] = merged_['salary'] + merged_['bonus']
    print(f"{merged_.groupby('department_name')['total_salary'].sum().sort_values(ascending=False)}")

#Find the department with the highest total salary + bonus
if False:
    merged_ = employees_data_frame.merge(salary_data_frame, on='employee_id').merge(department_data_frame, on='department_id')
    merged_['total_salary'] = merged_['salary'] + merged_['bonus']
    print(f"{merged_.loc[merged_['total_salary'].idxmax()][['employee_name','department_name']]}")



prices_data = {
    'product_id': [1, 1, 2, 2, 3, 3],
    'start_date': pandas.to_datetime(['2023-01-01', '2023-02-01', '2023-01-01', '2023-02-01', '2023-01-01', '2023-02-01']),
    'end_date': pandas.to_datetime(['2023-01-31', '2023-02-28', '2023-01-31', '2023-02-28', '2023-01-31', '2023-02-28']),
    'price': [100.0, 110.0, 90.0, 95.0, 120.0, 125.0]
}
prices_data_frame = pandas.DataFrame(prices_data)

units_sold_data = {
    'product_id': [1, 2, 3, 2, 1],
    'purchase_date': pandas.to_datetime(['2023-01-15', '2023-01-20', '2023-02-10', '2023-02-15', '2023-02-25']),
    'units': [5, 8, 12, 10, 6]
}
units_sold_data_frame = pandas.DataFrame(units_sold_data)



#Merged asof

#Calculate the average selling price for each product based on units_sold data
if False:
    prices_data_frame.sort_values('start_date', inplace=True)
    units_sold_data_frame.sort_values('purchase_date', inplace=True)

    merged_data = pandas.merge_asof(units_sold_data_frame, prices_data_frame, by='product_id', left_on='purchase_date', right_on='start_date')

    merged_data['total_price'] = merged_data['price'] * merged_data['units']
    total_units_sold = merged_data.groupby('product_id')['units'].sum()
    total_revenue = merged_data.groupby('product_id')['total_price'].sum()
    average_price = total_revenue / total_units_sold
    print(f"{average_price}")

#Find the number of units sold for each product in january 2023
if False:
    prices_data_frame.sort_values('start_date', inplace=True)
    units_sold_data_frame.sort_values('purchase_date', inplace=True)

    merged_data = pandas.merge_asof(units_sold_data_frame, prices_data_frame, by='product_id', left_on='purchase_date', right_on='start_date')
    jan_units = merged_data.loc[(merged_data['start_date'] >= '2023-01-01') & (merged_data['end_date'] < '2023-02-01')]
    print(f"{jan_units.groupby('product_id')['units'].sum()}")

#Find the revenue generated from product sales in february 2023
if False:
    prices_data_frame.sort_values('start_date', inplace=True)
    units_sold_data_frame.sort_values('purchase_date', inplace=True)

    merged_data = pandas.merge_asof(units_sold_data_frame, prices_data_frame, by='product_id', left_on='purchase_date', right_on='start_date')
    feb_ = merged_data.loc[(merged_data['start_date'] >= '2023-02-01') & (merged_data['end_date'] < '2023-03-01')]
    feb_['product_total'] = feb_['units'] * feb_['price']

    print(f"{feb_['product_total'].sum()}")

#Find the product with the highest average selling price
if False:
    prices_data_frame.sort_values('start_date', inplace=True)
    units_sold_data_frame.sort_values('purchase_date', inplace=True)

    merged_data = pandas.merge_asof(units_sold_data_frame, prices_data_frame, by='product_id', left_on='purchase_date', right_on='start_date')
    merged_data['total_price'] = merged_data['units'] * merged_data['price']
    
    total_units_sold = merged_data.groupby('product_id')['units'].sum()
    total_revenue = merged_data.groupby('product_id')['total_price'].sum()
    average_price = total_revenue / total_units_sold
    
    print(f"{average_price.idxmax()}")

#What were the prices and units sold for each product on their respective purchase dates
if False:
    prices_data_frame.sort_values('start_date', inplace=True)
    units_sold_data_frame.sort_values('purchase_date', inplace=True)
    merged_data = pandas.merge_asof(units_sold_data_frame, prices_data_frame, by='product_id', left_on='purchase_date', right_on='start_date')
    print(f"{merged_data[['product_id','purchase_date','price','units']]}")

#How many units of each product were sold, considering the price prevailing at the start of the month of the purchase
if False:
    prices_data_frame.sort_values('start_date', inplace=True)
    units_sold_data_frame.sort_values('purchase_date', inplace=True)
    merged_data = pandas.merge_asof(units_sold_data_frame, prices_data_frame, by='product_id', left_on='purchase_date', right_on='start_date')
    merged_data['units_total_price'] = merged_data['units'] * merged_data['price']
    print(f"{merged_data[['product_id','purchase_date','units_total_price']]}")

#What are the prices of products just before their respective purchase dates
if False:
    prices_data_frame.sort_values('start_date', inplace=True)
    units_sold_data_frame.sort_values('purchase_date', inplace=True)
    merged_data = pandas.merge_asof(units_sold_data_frame, prices_data_frame, by='product_id', left_on='purchase_date', right_on='end_date')

    print(f"{merged_data[['product_id','purchase_date', 'price']]}")