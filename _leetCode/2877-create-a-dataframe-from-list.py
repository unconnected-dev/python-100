#Create A DataFrame From List
#https://leetcode.com/problems/create-a-dataframe-from-list/description/
import pandas

case_ = [[1,15],[2,11],[3,11],[4,20]]

if False:
    def createDataframe(student_data):
        col_names = ['student_id', 'age']
        data = pandas.DataFrame(student_data, columns=col_names)
        return data

if True:
    def createDataframe(student_data):
        return pandas.DataFrame(student_data, columns=['student_id', 'age'])

print(f"{createDataframe(case_)}")