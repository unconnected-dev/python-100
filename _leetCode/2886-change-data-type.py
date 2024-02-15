#Change Data Type
#https://leetcode.com/problems/change-data-type/description/
import pandas

caseData = {
    "student_id": [1, 2],
    "name": ["Ava", "Kate"],
    "age": [6, 15],
    "grade": [73.0, 87.0]
}

caseDataFrame = pandas.DataFrame(caseData)

if False:
    def changeDatatype(students):
        students = students.astype({'grade': 'int'})
        return students

if True:
    def changeDatatype(students):
        students['grade'] = students[['grade']].astype(int)
        return students
    
print(f"{changeDatatype(caseDataFrame)}")