#Rehshape Data: Concetenate
#https://leetcode.com/problems/reshape-data-concatenate/description/
import pandas

caseData_1 = {
    "student_id": [1, 2, 3, 4],
    "name": ["Mason", "Ava", "Taylor", "Georgia"],
    "age": [8, 6, 15, 17]
}

caseData_2 = {
    "student_id": [5, 6],
    "name": ["Leo", "Alex"],
    "age": [7, 7]
}

df1_ = pandas.DataFrame(caseData_1)
df2_ = pandas.DataFrame(caseData_2)

if False:
    def fillMissingValues(df1, df2):
        df3 = pandas.concat([df1, df2])
        return df3

if True:
    def fillMissingValues(df1, df2):
        #ignore_index controls whether to reset the index of the resulting dataframe
        #to have a continuous range of integers starting from 0 or to retain the
        #original indicies

        #When set to true, the resulting dataframe will have its index reset to a
        #new continuous range starting from 0
        df3 = pandas.concat([df1, df2], ignore_index=True)
        return df3

print(f"{fillMissingValues(df1_, df2_)}")