import pandas

data_left = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
df_left = pandas.DataFrame(data_left)

data_right = {'A': [2, 3, 4], 'C': ['x', 'y', 'z']}
df_right = pandas.DataFrame(data_right)



#Left Join
#A left join includes all the rows from the left dataframe and only the matching
#rows from the right dataframe. If there are no matching rows in the right 
#dataframe we still include the row from the left, filling in missing values
#for the columns on the right
if False:
    left_join_result = pandas.merge(df_left, df_right, on='A', how='left')
    print(f"{left_join_result}")

#Inner Join
#An inner join only includes rows where there is a match between the common 
#columns in both dataframes
if False:
    inner_join_result = pandas.merge(df_left, df_right, on='A', how='inner')
    print(f"{inner_join_result}")

#Outer Join
#Also known as a full outer join. Includes all rows and columns from both
#dataframes. Regardless of whether there is a match or not. 
#If there is a match it includes matched rows. If there's no match it
#includes the rows from one dataframe, filling missing values from the
#other dataframe
if False:
    outer_join_result = pandas.merge(df_left, df_right, on='A', how='outer')
    print(f"{outer_join_result}")