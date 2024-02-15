#Rename Columns
#https://leetcode.com/problems/rename-columns/description/
import pandas

caseData = {
    "id": [1, 2, 3, 4, 5],
    "first": ["Mason", "Ava", "Taylor", "Georgia", "Thomas"],
    "last": ["King", "Wright", "Hall", "Thompson", "Moore"],
    "age": [6, 7, 16, 18, 10]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def renameColumns(students):
        students.columns = ["student_id", "first_name", "last_name", "age_in_years"]
        return students
    
print(f"{renameColumns(caseDataFrame).to_markdown(index=False)}")