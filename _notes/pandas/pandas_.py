#Pandas
#Is a Python library that provides high-performance easy to use data structures and data
#analysis tools for manipulating and analyzing data

#The key components of Pandas are in its two primary data structures

#Series: A one-dimensional labeled array capable of holding any data type
#similar to a list

#DataFrame: A two-dimensional labeled data structure made of rows and columns
#similar to a spreadsheet


#Do not name the notes file pandas.py
import pandas

#Basics 
if True:
    
    #Reading from a CSV file
    csv_relative_file_path = "./_notes/pandas/file_data/read_from/random_data.csv"
    with open(csv_relative_file_path) as csv_file:
        csv_data = pandas.read_csv(csv_file)

    print(csv_data)
