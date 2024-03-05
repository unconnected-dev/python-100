import pandas

sales_data = {
    'Date': pandas.to_datetime(['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03']),
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'Price': [100, 50, 120, 45, 110, 55],
    'Quantity': [2, 3, 1, 2, 3, 1]
}
sales_dataframe = pandas.DataFrame(sales_data)



#What is the total sales revenue per day
if False:
    total_sales_per_day = sales_dataframe.groupby('Date').agg({'Price': 'sum'})
    print(f"{total_sales_per_day}")

#What is the average price and total quantity sold for each product
if False:
    stats = sales_dataframe.groupby('Product').agg({'Price':'mean','Quantity':'sum'})
    print(f"{stats}")

#What is the total sales revenue and average price per category
if False:
    sales_dataframe['revenue'] = sales_dataframe['Price'] * sales_dataframe['Quantity']
    stats = sales_dataframe.groupby('Category').agg({'Price': 'mean', 'revenue':'sum'})
    print(f"{stats}")

#What is the highest and lowest price for each product
if False:
    price_per_product = sales_dataframe.groupby('Product').agg({'Price':['max','min']})
    print(f"{price_per_product}")