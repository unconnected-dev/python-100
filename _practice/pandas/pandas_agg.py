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

#What is the total sales revenue and average price per day for each category
if False:
    sales_dataframe['revenue'] = sales_dataframe['Price'] * sales_dataframe['Quantity']
    sales_per_day = sales_dataframe.groupby(['Date','Category']).agg({'revenue':'sum','Price':'mean'})
    print(f"{sales_per_day}")

#What is the total sales revenue for each product category per day
if False:
    sales_dataframe['revenue'] = sales_dataframe['Price'] * sales_dataframe['Quantity']
    total_sales = sales_dataframe.groupby('Category').agg({'revenue':'sum'})
    print(f"{total_sales}")

#What is the max min quantity sold for each product category
if False:
    stats = sales_dataframe.groupby('Category').agg({'Quantity':['max','min']})
    print(f"{stats}")

#What is the average price and total quantity sold per day for each product category
if False:
    avg_price = sales_dataframe.groupby(['Date','Category']).agg({'Price':'mean','Quantity':'sum'})
    print(f"{avg_price}")

#What is the total sales revenue for each product category across all dates
if False:
    sales_dataframe['revenue'] = sales_dataframe['Price'] * sales_dataframe['Quantity']
    print(f"{sales_dataframe.groupby('Category').agg({'revenue':'sum'})}")

#Which product has the highest total sales revenue
if False:
    #So total_sales is the column name
    highest_sales_product = sales_dataframe.groupby('Product').agg(total_sales=('Price','sum')).idxmax()
    print(f"{highest_sales_product[0]}")

#What is the average price and total quantity sold for each category of products
if False:
    avg_ = sales_dataframe.groupby('Category').agg(avg_price=('Price','mean'),total_sold=('Quantity','sum'))
    print(f"{avg_}")

#What is the total sales revenue and average price per day for each product
if False:
    sales_dataframe['revenue'] = sales_dataframe['Price'] * sales_dataframe['Quantity']
    stats = sales_dataframe.groupby('Product').agg(total_sales=('revenue','sum'),avg_price=('Price','mean'))
    print(f"{stats}")