#Employees With Missing Information
#https://leetcode.com/problems/employees-with-missing-information/description/
import pandas

employeesData = {

    "employee_id": [2, 4, 5],
    "name": ["Crew", "Haven", "Kristian"]
}

salariesData = {

    "employee_id": [5, 1, 4],
    "salary": [76071, 22517, 63539]
}

employeesDataFrame = pandas.DataFrame(employeesData)
salariesDataFrame = pandas.DataFrame(salariesData)

if True:
    def find_employees(employees: pandas.DataFrame, salaries: pandas.DataFrame) -> pandas.DataFrame:
        table_1 = employees.loc[~employees['employee_id'].isin(salaries['employee_id']), ['employee_id']]
        table_2 = salaries.loc[~salaries['employee_id'].isin(employees['employee_id']), ['employee_id']]
        row_concat = pandas.concat([table_1, table_2])
        return row_concat.sort_values(by='employee_id')

if True:
    def find_employees(employees: pandas.DataFrame, salaries: pandas.DataFrame) -> pandas.DataFrame:
        dataFrame = pandas.merge(employees, salaries, on='employee_id', how='outer')
        return dataFrame[dataFrame.isna().any(axis=1)][['employee_id']].sort_values(by='employee_id')

print(f"{find_employees(employeesDataFrame, salariesDataFrame)}")