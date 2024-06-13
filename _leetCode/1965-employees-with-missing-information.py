#Employees With Missing Information
#https://leetcode.com/problems/employees-with-missing-information/description/
import pandas


if True:
    def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
        table_1 = employees.loc[~employees['employee_id'].isin(salaries['employee_id']), ['employee_id']]
        table_2 = salaries.loc[~salaries['employee_id'].isin(employees['employee_id']), ['employee_id']]
        row_concat = pandas.concat([table_1, table_2])
        return row_concat.sort_values(by='employee_id')