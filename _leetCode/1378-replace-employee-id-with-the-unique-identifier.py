#Replace Employee ID With The Unique Identifier
#https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/
import pandas

employees_data = {
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
}
employees_dataframe = pandas.DataFrame(employees_data)

employee_uni_data = {
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
}
employee_uni_dataframe = pandas.DataFrame(employee_uni_data)

if False:
    def replace_employee_id(employees, employee_uni):
        merged_ = employees.merge(employee_uni, on='id', how='left')
        return merged_[['unique_id','name']]
    
if True:
    def replace_employee_id(employees, employee_uni):
        return pandas.merge(employees, employee_uni, on='id', how='left')[['unique_id', 'name']]

print(f"{replace_employee_id(employees_dataframe, employee_uni_dataframe)}")