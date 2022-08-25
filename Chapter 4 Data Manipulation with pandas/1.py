'''
Inspecting a DataFrame

When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. There are several useful methods and attributes for this.

    .head() returns the first few rows (the “head” of the DataFrame).
    .info() shows information on each of the columns, such as the data type and number of missing values.
    .shape returns the number of rows and columns of the DataFrame.
    .describe() calculates a few summary statistics for each column.

'''
# homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018.

# Print the head of the homelessness data
import pandas as pd
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

'''
Parts of a DataFrame

To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:

    .values: A two-dimensional NumPy array of values.
    .columns: An index of columns: the column names.
    .index: An index for the rows: either row numbers or row names.

You can usually think of indexes as a list of strings or numbers, though the pandas Index data type allows for more sophisticated options. (These will be covered later in the course.)
'''

# Import pandas using the alias pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

