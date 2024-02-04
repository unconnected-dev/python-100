#Create A New Column
#https://leetcode.com/problems/create-a-new-column/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas

caseData = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def createBonusColumn(employees):
        employees["bonus"] = employees["salary"] * 2
        return employees
    
print(f"{createBonusColumn(caseDataFrame).to_markdown(index=False)}")