import pandas
import numpy

sales_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05','2023-01-06', '2023-01-07', '2023-01-08'],
    'Product': ['Laptop', 'Smartphone', 'Laptop', 'Headphones', 'Smartphone','Tablet', 'Laptop', 'Smartwatch'],
    'Quantity_Sold': [100, numpy.nan, 90, 80, 110, numpy.nan, numpy.nan, numpy.nan],
    'Revenue': [5000, 6000, 4500, 4000, numpy.nan, numpy.nan, numpy.nan, numpy.nan],
    'Profit': [1000, None, 900, None, 1100, numpy.nan, numpy.nan, numpy.nan],
    'Region': ['North', 'West', 'East', 'South', 'North', None, 'East', 'South']
}
sales_data_frame = pandas.DataFrame(sales_data)


#How many missing values are there in the quanity_sold column?
if False:
    print(f"{sales_data_frame['Quantity_Sold'].isna().sum()}")

if False:
    print(f"{sales_data_frame.loc[sales_data_frame['Quantity_Sold'].isna()].shape[0]}")

#What percentage of the revenue column contains missing values
if False:
    percentage = (sales_data_frame['Revenue'].isna().sum() / len(sales_data_frame)) * 100
    print(f"{percentage}")

#Drop all rows with any missing values and display the resulting dataframe
if False:
    print(f"{sales_data_frame.dropna()}")

#Replace all the missing values in profit with 0
if False:
    sales_data_frame['Profit'].fillna(0, inplace=True)
    print(f"{sales_data_frame}")

#Fill missing values in quantity sold column with mean of the column
if False:
    m = sales_data_frame['Quantity_Sold'].mean()
    sales_data_frame['Quantity_Sold'].fillna(m, inplace=True)
    print(f"{sales_data_frame}")

#Replace all missing values in the dataframe with string 'Unknown'
if False:
    sales_data_frame.fillna('Unknown', inplace=True)
    print(f"{sales_data_frame}")

#Check if there are any missing values in the dataframe
if False:
    any_missing = sales_data_frame.isna().any().any()
    print(f"{any_missing}")

#Count the number of non missing values in each column
if False:
    non_missing = sales_data_frame.count()
    print(f"{non_missing}")

#Check if there are any missing values in the date column
if False:
    any_missing = sales_data_frame['Date'].isna().any()
    print(f"{any_missing}")

#Fill missing values in the revenue column with the median of the column
if False:
    med = sales_data_frame['Revenue'].median()
    sales_data_frame['Revenue'].fillna(med, inplace=True)
    print(f"{sales_data_frame}")

#Count the number of missing values in each column of the dataframe
if False:
    print(f"{sales_data_frame.isnull().sum()}")

#Remove rows with any missing values from the dataframe
if False:
    sales_data_frame.dropna(inplace=True)
    print(f"{sales_data_frame}")

#Fill missing values in the quantity sold column with the mean of the column
if False:
    mean_ = sales_data_frame['Quantity_Sold'].mean()
    sales_data_frame['Quantity_Sold'].fillna(mean_, inplace=True)
    print(f"{sales_data_frame}")

#Replace missing values in the revenue column with 0
if False:
    sales_data_frame['Revenue'].fillna(0, inplace=True)
    print(f"{sales_data_frame}")

#Fill missing values in the profit column with the median of the column
if False:
    median_ = sales_data_frame['Profit'].median()
    sales_data_frame['Profit'].fillna(median_, inplace=True)
    print(f"{sales_data_frame}")

#Replace missing values in the region column with a default value 'unknown'
if False:
    sales_data_frame['Region'].fillna('Unknown', inplace=True)
    print(f"{sales_data_frame}")

#Drop columns with any missing values
if False:
    sales_data_frame.dropna(inplace=True, axis=1)
    print(f"{sales_data_frame}")

#Drop rows with any missing values
if False:
    sales_data_frame.dropna(inplace=True)
    print(f"{sales_data_frame}")

#Check if there are any missing values in the dataframe
if False:
    r = sales_data_frame.isna().any().any()
    print(f"{r}")

if False:
    r = sales_data_frame.isnull().values.any()
    print(f"{r}")

#Interpolate missing values in the profit column using linear interpolation
if False:
    sales_data_frame['Profit'].interpolate(method='linear', inplace=True)
    print(f"{sales_data_frame}")

#Filter out rows where both quantity sold and revenue are missing
if False:
    sales_filtered = sales_data_frame.dropna(subset=['Quantity_Sold', 'Revenue'], how='all')
    print(f"{sales_filtered}")

#Remove rows where both revenue and profit columns are missing
if False:
    sales_data_frame.dropna(subset=['Revenue','Profit'], inplace=True, how='all')
    print(f"{sales_data_frame}")

#Drop rows where product is missing
if False:
    sales_data_frame.dropna(subset=['Product'], inplace=True, how='all')
    print(f"{sales_data_frame}")

#Fill missing values in the profit column with the forward fill method
if False:
    res = sales_data_frame['Profit'].ffill()
    print(f"{res}")

#How many missing values are there in each column
if False:
    total = sales_data_frame.isna().sum().sum()
    print(f"{total}")

#What is the total revenue generated on each date
if False:
    revenue_per_date = sales_data_frame.groupby('Date')['Revenue'].sum()
    print(revenue_per_date)

#Fill missing values in quantity sold with the mean quantity sold
if False:
    m_ = sales_data_frame['Quantity_Sold'].mean()
    sales_data_frame['Quantity_Sold'].fillna(m_, inplace=True)
    print(f"{sales_data_frame}")

#What is the average profit generated by each product
if False:
    print(f"{sales_data_frame.groupby('Product')['Profit'].mean()}")

#Drop rows where region is missing
if False:
    print(f"{sales_data_frame.dropna(subset=['Region'])}")

#Fill missing values in profit with the median profit
if False:
    p_ = sales_data_frame['Profit'].median()
    sales_data_frame['Profit'].fillna(p_, inplace=True)
    print(f"{sales_data_frame}")

#What is the total quantity sold in each region
if False:
    print(f"{sales_data_frame.groupby('Region')['Quantity_Sold'].sum()}")

#Drop any missing columns with any missing values
if False:
    print(f"{sales_data_frame.dropna(axis=1)}")

#Forward fill missing values in region
if False:
    sales_data_frame['Region'].ffill(inplace=True)
    print(f"{sales_data_frame}")

if False:
    sales_data_frame['Region'].fillna(method='ffill', inplace=True)
    print(f"{sales_data_frame}")