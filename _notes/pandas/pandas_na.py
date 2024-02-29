import pandas
import numpy

exampleData = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05','2023-01-06', '2023-01-07', '2023-01-08'],
    'Product': ['Laptop', 'Smartphone', 'Laptop', 'Headphones', 'Smartphone','Tablet', 'Laptop', 'Smartwatch'],
    'Quantity_Sold': [100, numpy.nan, 90, 80, 110, numpy.nan, numpy.nan, numpy.nan],
    'Revenue': [5000, 6000, 4500, 4000, numpy.nan, numpy.nan, numpy.nan, numpy.nan],
    'Profit': [1000, None, 900, None, 1100, numpy.nan, numpy.nan, numpy.nan],
    'Region': ['North', 'West', 'East', 'South', 'North', None, 'East', 'South']
}

df = pandas.DataFrame(exampleData)


#Missing Values (NA) Handling



#Detecting Missing Values
if False:
    print(f"{df['Quantity_Sold'].isna()}")

if False:
    print(f"{df['Quantity_Sold'].notnull()}")



#Counting Missing Values
if False:
    #How many missing values in quantity sold
    print(f"{df['Quantity_Sold'].isna().sum()}")

if False:
    #How many missing values in each column
    print(f"{df.isna().sum()}")

if False:
    #Total number of missing values
    print(f"{df.isna().sum().sum()}")



#Handling Missing Values
if False:
    #Drops all rows with any missing value
    print(f"{df.dropna()}")

if False:
    #Drops all columns with any missing value
    print(f"{df.dropna(axis=1)}")

if False:
    #Drop rows where both quantity sold and revenue are missing
    print(f"{df.dropna(subset=['Quantity_Sold','Revenue'], how='all')}")

if False:
    #Fill missing values with particular value
    print(f"{df['Region'].fillna('Unknown')}")

if False:
    #Fill missing values with forward fill method
    print(f"{df['Profit'].ffill()}")



#Group-Specific Handling
if False:
    #Fill missing values in quanitity sold column with the mean of each product group
    df['Quantity_Sold'] = df.groupby('Product')['Quantity_Sold'].transform(lambda x: x.fillna(x.mean()))
    print(f"{df}")

if False:
    #Fill missing values in revenue column with the median of each product group
    df['Revenue'] = df.groupby('Product')['Revenue'].transform(lambda x: x.fillna(x.median()))
    print(f"{df}")



#Interpolation Methods
if False:
    #Interpolate missing values in the profit column using linear interpolation
    df['Profit'].interpolate(method='linear', inplace=True)
    print(f"{df}")

if False:
    #Fill missing values, estimating them based on a curve that best fits the existing data points
    df['Profit'].interpolate(method='polynomial', order=2, inplace=True)
    print(f"{df}")