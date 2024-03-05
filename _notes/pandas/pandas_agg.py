import pandas

sales_data = {
    'Date': pandas.to_datetime(['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03']),
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'Price': [100, 50, 120, 45, 110, 55],
    'Quantity': [2, 3, 1, 2, 3, 1]
}
sales_dataframe = pandas.DataFrame(sales_data)



#Agg Function
#Agg is short for aggregate and it is used to perform aggregation operations on data in pandas
#It is used to compute multiple aggregate statistics simultaneously, making it efficient for
#summarizing data across different groups or categories. 


#Basic Agg
if False:
    result_ = sales_dataframe.groupby('Date').agg({'Price': 'sum'})
    print(f"{result_}")

#Multiple Computations On Single Column Data
if False:
    result_ = sales_dataframe.groupby('Product').agg({'Price':['max','min']})
    print(f"{result_}")

#Computations On Different Columns
if False:
    result_ = sales_dataframe.groupby(['Date','Category']).agg({'Price':'mean','Quantity':'sum'})
    print(f"{result_}")

#Assigning Column Names
if False:
    result_ = sales_dataframe.groupby('Category').agg(avg_price=('Price','mean'), total_sold=('Quantity','sum'))
    result_.rename(columns={'avg_price': 'Average Price'}, inplace=True)
    print(f"{result_}")



#When using agg, missing values in columns being aggregated are ignored. They are
#skipped over and the result is based on the available data points.

#If there are missing values in the grouping columns (columns used for grouping via groupby)
#pandas retains these missing values in the resulting grouped DataFrame. This means that rows
#with missing values in the grouping columns will form separate groups in the output DataFrame.



data = {
    'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'B'],
    'Value': [1, 2, 3, pandas.NA, 5, pandas.NA, 7]
}
dataframe_ = pandas.DataFrame(data)

#In the example agg calculates the sum of non-missing values for each category
if False:
    result_ = dataframe_.groupby('Category').agg(sum_value=('Value', 'sum'))
    print(f"{result_}")