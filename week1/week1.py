# learnt to download and import data analysis libraris in python 
# they are: pandas, numpy, matplotlib, seaborne, 
# also jupyter for a coding environment but can also use vs code 
# we use pip install <name>

# importing them 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading a dataset we use pandas for this
# we can load from a url or a local file
 
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv') # online file
#df = pd.read_csv('file path') # if local file

# exploring the data
print(df.head()) # first 5 rows
print(df.info()) # info about data types and non-null counts
print(df.describe()) # statistical summary of numerical columns
print(df.columns) # column names
print(df.shape) # number of rows and columns
print(df.isnull().sum()) # check for missing values
print(df['species'].value_counts()) # count of unique values in a column

# handle missing values
df = df.dropna() # drop rows with missing values
df = df.fillna(method='ffill') # forward fill missing values
df = df.fillna(method='bfill') # backward fill missing values
df = df.fillna(df.mean()) # fill with mean of the column
df = df.fillna(df.median()) # fill with median of the column
df = df.fillna(df.mode().iloc[0]) # fill with mode of the column
df['column_name'] = df['column_name'].fillna(value) # fill with a specific value
df['column_name'] = df['column_name'].interpolate() # interpolate missing values
df['column_name'] = df['column_name'].replace(to_replace, value) # replace specific values
df['column_name'] = df['column_name'].astype(data_type) # change data type of a column

# filtering and sorting data 



