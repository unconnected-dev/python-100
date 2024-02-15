#Drop Missing Data
#https://leetcode.com/problems/drop-missing-data/description/
import pandas

caseData = {
    "student_id": [32, 217, 779, 849],
    "name": ["Piper", None, "Georgia", "Willow"],
    "age": [5, 19, 20, 14]
}

caseDataFrame = pandas.DataFrame(caseData)

if False:
    def dropMissingData(students):
        #Returns a new DataFrame with missing values removed
        students = students.dropna()
        return students

if True:
    def dropMissingData(students):
        students = students.dropna(subset='name')
        return students

print(f"{dropMissingData(caseDataFrame).to_markdown(index=False)}")