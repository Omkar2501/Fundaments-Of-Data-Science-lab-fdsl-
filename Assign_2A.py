import pandas as pd
import numpy as np

data=pd.read_csv('Employee.csv')
data1=pd.read_excel('Employee.xlsx')
print(data)
print(data1)
print(data.head())  #prints the first 5 rows of the data
print(data.tail()) #prints the last 5 rows of the data
print(data.shape) #prints the number of rows and columns in the data
print(data.info()) #prints the summary of the data
print(data.describe()) #prints the statistical summary of the data

print("First 3 rows:",data.head(3))

# loc: label-based selection
print("loc example (rows 0-2 specific columns):")
print(data.loc[0:2,['Employee ID','Employee Name']]) #prints the first 3 rows of the data with specific columns

# iloc: position-based selection
print("\n iloc example (first 3 rows ,first 3 columns):")
print(data.iloc[0:3, 0:3]) #prints the first 3 rows and first 3 columns of the data

# Boolean indexing: filter rows where Region is 'East'
print("\nBoolean indexing (Region == 'East'):")
print(data[data["Region"] == "East"])
