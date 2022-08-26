"""
Setting and removing indexes

pandas allows you to designate columns as an index. 
This enables cleaner code when taking subsets (as well as providing more efficient lookup under some circumstances).

"""

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))


"""
Subsetting with .loc[]

The killer feature for indexes is .loc[]: a subsetting method that accepts index values. 
When you pass it a single argument, it will take a subset of rows.

The code for subsetting using .loc[] can be easier to read than standard square bracket subsetting, 
which can make your code less burdensome to maintain.
"""

# Create a list called cities that contains "Moscow" and "Saint Petersburg".
# Use[] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
# Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# way 1 Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[], this way is more readable than the previous way : way 1
print(temperatures_ind.loc[cities])

"""
Setting multi-level indexes

Indexes can also be made out of multiple columns, forming a multi-level index (sometimes called a hierarchical index). 
There is a trade-off to using these. 

The benefit is that multi-level indexes make it more natural to reason about nested categorical variables. 
For example, in a clinical trial, you might have control and treatment groups. Then each test subject belongs to one 
or another group, and we can say that a test subject is nested inside the treatment group. 
Similarly, in the temperature dataset, the city is located in the country, so we can say a city is nested inside the country.

The main downside is that the code for manipulating indexes is different from the code for manipulating columns, so you have to learn two syntaxes and keep track of how your data is represented.

"""

# Set the index of temperatures to the "country" and "city" columns, and assign this to temperatures_ind.
# Specify two country/city pairs to keep: "Brazil"/"Rio De Janeiro" and "Pakistan"/"Lahore", assigning to rows_to_keep.
# Print and subset temperatures_ind for rows_to_keep using .loc[].

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [["Brazil", "Rio De Janeiro"], ["Pakistan", "Lahore"]]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])


"""
Sorting by index values
Previously, you changed the order of the rows in a DataFrame by calling .sort_values(). 
It's also useful to be able to sort by elements in the index. For this, you need to use .sort_index().
"""

# Sort temperatures_ind by the index values.
# Sort temperatures_ind by the index values at the "city" level.
# Sort temperatures_ind by ascending country then descending city.


# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country","city"], ascending=[True,False]))


"""
Slicing index values

Slicing lets you select consecutive elements of an object using first:last syntax. DataFrames can be sliced by index values 
or by row/column number; we'll start with the first case. This involves slicing inside the .loc[] method.

Compared to slicing lists, there are a few things to remember.

    You can only slice an index if the index is sorted (using .sort_index()).
    To slice at the outer level, first and last can be strings.
    To slice at inner levels, first and last should be tuples.
    If you pass a single slice to .loc[], it will slice the rows.

"""

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow: (outer_level, inner_leve) : ...
print(temperatures_srt.loc[ ("Pakistan","Lahore") : ("Russia","Moscow")])


"""
Slicing in both directions

You've seen slicing DataFrames by rows and by columns, but since DataFrames are two-dimensional objects, it is often natural 
to slice both dimensions at once. 
That is, by passing two arguments to .loc[], you can subset by rows and columns in one go.
"""

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[
    ("India", "Hyderabad"): ("Iraq", "Baghdad"),  # rows
    "date":"avg_temp_c"  # columns
])


"""
Slicing time series

Slicing is particularly useful for time series since it's a common thing to want to filter for data within a date range. 
Add the date column to the index, then use .loc[] to perform the subsetting. 
The important thing to remember is to keep your dates in ISO 8601 format, that is, "yyyy-mm-dd" for year-month-day, 
"yyyy-mm" for year-month, and "yyyy" for year.

"""
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") &
                                 (temperatures["date"] <= "2011-12-31")
                                 ]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])


"""
Subsetting by row/column number
The most common ways to subset rows are the ways we've previously discussed: using a Boolean condition or by index labels. However, it is also occasionally useful to pass row numbers.

This is done using .iloc[], and like .loc[], it can take two arguments to let you subset by rows and columns.
"""

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:5, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:, 2:4])


'''
# Add a year column to temperatures
It's interesting to see how temperatures for each city change over time—looking at every month results in a big table, 
which can be tricky to reason about. Instead, let's look at how temperatures change by year.

You can access the components of a date (year, month and day) using code of the form dataframe["column"].dt.component. 
For example, the month component is dataframe["column"].dt.month, and the year component is dataframe["column"].dt.year.

Once you have the year column, you can create a pivot table with the data aggregated by city and year, which you'll explore in the coming exercises
'''

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# See the result
print(temp_by_country_city_vs_year)


'''
Subsetting pivot tables

A pivot table is just a DataFrame with sorted indexes, so the techniques you have learned already can be used to subset them. 
In particular, the .loc[] + slicing combination is often helpful.
'''

# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India", "Delhi")]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India", "Delhi"), 2005:2010]


'''
Calculating on a pivot table

Pivot tables are filled with summary statistics, but they are only a first step to finding something insightful. 
Often you'll need to perform further calculations on them. 
A common thing to do is to find the rows or columns where the highest or lowest value occurs
'''

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()
    
# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])