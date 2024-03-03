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


#Concat
#This is not used for joining dataframes. It is used for concatenating
#or stacking dataframes along rows(vertically) or columns(horizontally)

#It is useful when you have dataframes that have the same columns (for vertical concatentation)
#or the same index (for horizontal concatenation)
if False:
    row_concat = pandas.concat([df_left, df_right])
    print(f"{row_concat}")

if False:
    col_concat = pandas.concat([df_left, df_right], axis=1)
    print(f"{col_concat}")



sales_data = {
    'product_id': [1, 2, 3, 1, 2],
    'sale_date': pandas.to_datetime(['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-15']),
    'units_sold': [5, 8, 3, 6, 10]
}
sales_data_frame = pandas.DataFrame(sales_data)

price_data = {
    'product_id': [1, 2, 1, 2, 3],
    'price_date': pandas.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']),
    'price': [100.0, 110.0, 95.0, 105.0, 120.0]
}
prices_data_frame = pandas.DataFrame(price_data)


#Merged asof
#This is a specialized merge operation used to merge two datasets based on the
#nearest keys rather than exact matches

#by='product_id', indicates merge based on product_id
#left_on='sales_date', specifies the sale_date column in sales_data_frame will be used for merging
#right_on='price_date', specifies the price_date column in price_data_frame will be used for merging

#The merge is based on the closest date. For each row in sales_data_frame the corresponding row in
#prices_data_frame with the closest date (but not after sales date) and matching product_id
#is merged

if False:
    merged_data = pandas.merge_asof(sales_data_frame, prices_data_frame, by='product_id', left_on='sale_date', right_on='price_date')
    print(f"{merged_data}")