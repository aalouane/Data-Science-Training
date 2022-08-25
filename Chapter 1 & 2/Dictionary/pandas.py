'''
High level data manipulation data
wes McKinny
Built on Numpy
dataFrame

csv = comma-separated values
'''

# --------------- Dictionary to DataFrame (1)----------------------------
'''
Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python.
The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.
'''
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict  = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars
print(cars)

# ----------------- Dictionary to DataFrame (2) -----------------------------
'''
Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. What if you're dealing with millions of observations? 
In those cases, the data is typically available as files with a regular structure. One of those file types is the CSV file, which is short for "comma-separated values".

To import CSV data into Python as a Pandas DataFrame you can use read_csv().

Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used as a row label? Well, that's exactly what you need here!
'''

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)

# ----------------------------------------
'''
Recap
Square brackets
    Columns acess: brics[["country", "capital"]]
    Row access : only through slicing brics[1:4]            | brics[:, [0,1]]

loc(label-based)                                            | iloc(integer position-based)
    Row access          brics.loc[["Ru", "IN", "CH"]]       | brics.iloc[[1,2,3]]
    Column access brics.loc[:, ["country", "capital"]]
    Row & Colmns access                                     | brics.iloc[[1,2,3], [0,1]]
        brics.loc[
            ["RU", "IN", "CH"],
            ["country", "capital"]
        ]

'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars.loc[:, ["country", "drives_right"]])

# Print out first 3 observations
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Print out drives_right value of Morocco
print(cars.loc[["MOR"], ["drives_right"]])

# Print sub-DataFrame
print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])

# Print out drives_right column as Series
print(cars.loc[:,"drives_right"])
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.loc[:, ["drives_right"]])
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ["cars_per_cap", "drives_right"]])
print(cars.iloc[:, [1,2]])

