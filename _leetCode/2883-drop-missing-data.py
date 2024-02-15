#Drop Missing Data
#https://leetcode.com/problems/drop-missing-data/description/
import pandas

caseData_1 = {
    "student_id": [32, 217, 779, 849],
    "name": ["Piper", None, "Georgia", "Willow"],
    "age": [5, 19, 20, 14]
}

caseData_2 = {
    "student_id": [355, 951, 470, 977, 300],
    "name": [None, None, "Quincy", "Sophia", "Liam"],
    "age": [9, 8, 20, None, 15]
}

caseDataFrame = pandas.DataFrame(caseData_2)

if False:
    #caseData_2 has missing data in name and age columns so all will be removed. 
    #The LeetCode question requires only the name column to be checked which 
    #requires subset
    def dropMissingData(students):
        #Returns a new DataFrame with missing values removed
        students = students.dropna()
        return students

if False:
    def dropMissingData(students):
        #Specify the columns to check for missing values
        students = students.dropna(subset='name')
        return students

if True:
    def dropMissingData(students):
        #df2 will have the indices of rows where students name column is missing
        #df2 is a Pandas index object
        df2 = students[students['name'].isnull()].index
        students.drop(df2, inplace = True)
        return students

print(f"{dropMissingData(caseDataFrame).to_markdown(index=False)}")