#Select Data
#https://leetcode.com/problems/select-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas

caseData = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def selectData(students):
        return students[students.student_id == 101][["name", "age"]]
    
print(f"{selectData(caseDataFrame).to_markdown(index=False)}")