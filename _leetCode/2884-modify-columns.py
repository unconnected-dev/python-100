#Modify Columns
#https://leetcode.com/problems/modify-columns/description/
import pandas

caseData = {
    "name": ["Jack", "Piper", "Mia", "Ulysses"],
    "salary": [19666, 74754, 62509, 54866]
}

caseDataFrame = pandas.DataFrame(caseData)

if False:
    def modifySalaryColumn(employees):
        employees['salary'] = employees['salary'] * 2
        return employees

if False:
    def modifySalaryColumn(employees):
        employees['salary'] *= 2
        return employees

if True:
    def modifySalaryColumn(employees):
        employees['salary'] = employees['salary'].mul(2)
        return employees

print(f"{modifySalaryColumn(caseDataFrame).to_markdown(index=False)}")