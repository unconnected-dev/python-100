#Employee Bonus
#https://leetcode.com/problems/employee-bonus/description/
import pandas

employeeData = {
    'empId': [3, 1, 2, 4],
    'name': ['Brad', 'John', 'Dan', 'Thomas'],
    'supervisor': [None, 3, 3, 3],
    'salary': [4000, 1000, 2000, 4000]
}
employeeDataFrame = pandas.DataFrame(employeeData)

bonusData = {
    'empId': [2, 4],
    'bonus': [500, 2000]
}
bonusDataFrame = pandas.DataFrame(bonusData)

if True:
    def employee_bonus(employee, bonus):
        merged_ = pandas.merge(employee, bonus, on='empId', how='outer')
        return merged_.loc[(merged_['bonus'].isna()) | (merged_['bonus'] < 1000), ['name','bonus']].sort_values(by='bonus', ascending=False)
    
print(f"{employee_bonus(employeeDataFrame, bonusDataFrame)}")
