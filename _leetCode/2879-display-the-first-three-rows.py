#Display The First Three Rows
#https://leetcode.com/problems/display-the-first-three-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas

caseEmployees = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

caseDataFrame = pandas.DataFrame(caseEmployees)

if True:
    def selectFirstRows(employees: pandas.DataFrame) -> pandas.DataFrame:
        return employees[0:3]
    
print(f"{selectFirstRows(caseDataFrame)}")