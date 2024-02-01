#Create A DataFrame From List
#https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas

case_ = [[1,15],[2,11],[3,11],[4,20]]

if True:
    def createDataframe(student_data):
        col_names = ['student_id', 'age']
        data = pandas.DataFrame(student_data, columns=col_names)
        return data

print(f"{createDataframe(case_)}")