import pandas
import numpy

sales_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Product': ['Laptop', 'Smartphone', 'Laptop', 'Headphones', 'Smartphone'],
    'Quantity_Sold': [100, numpy.nan, 90, 80, 110],
    'Revenue': [5000, 6000, 4500, 4000, numpy.nan],
    'Profit': [1000, None, 900, None, 1100]
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
if True:
    med = sales_data_frame['Revenue'].median()
    sales_data_frame['Revenue'].fillna(med, inplace=True)
    print(f"{sales_data_frame}")