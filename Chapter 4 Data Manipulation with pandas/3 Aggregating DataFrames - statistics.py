'''
Mean and median

Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. 
For example, mean, median, minimum, maximum, and standard deviation are summary statistics. 

Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it. 
'''

# Print the head of the sales DataFrame
import numpy as np
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())

# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())

# A custom IQR function


'''
Efficient summaries

While pandas and NumPy have tons of functions, sometimes, you may need a different function to summarize your data.

The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than one column 
of a DataFrame at once, making your aggregations super-efficient. 
For example, 

In the custom function for this exercise, "IQR" is short for inter-quartile range, which is the 75th percentile minus the 25th percentile. 
It's an alternative to standard deviation that is helpful if your data contains outliers.
'''
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))

# Import NumPy and create custom IQR function


def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

'''
Cumulative statistics

Cumulative statistics can also be helpful in tracking summary statistics over time. 
In this exercise, you'll calculate the cumulative sum and cumulative max of a department's weekly sales, which will allow you 
to identify what the total sales were so far as well as what the highest weekly sales were so far
'''

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date", ascending=True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

'''
Dropping duplicates

Removing duplicates is an essential skill to get accurate counts because often, you don't want to count the same thing multiple times. 
In this exercise, you'll create some new DataFrames using unique values from sales.
'''

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]
                      == True].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates["date"])

'''
Counting categorical variables

Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. 
In this exercise, you'll count the number of each type of store and the number of each department number using the DataFrames
 you created in the previous exercise:
'''

# Count the number of stores of each type
store_counts = store_types["type"].value_counts(sort=True)
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

'''
While .groupby() is useful, you can calculate grouped summary statistics without it. 
'''
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

'''
The .groupby() method makes life much easier. In this exercise, you'll perform the same calculations as last time, except you'll use the .groupby() method. You'll also perform calculations on data grouped by 
two variables to see if sales differ by store type depending on if it's a holiday week or not. 
'''
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales["weekly_sales"])
print(sales_propn_by_type)

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])[
    "weekly_sales"].sum()
print(sales_by_type_is_holiday)


# groupby and agg
# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")["unemployment", "fuel_price_usd_per_l"].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


"""
Pivot tables are the standard way of aggregating data in spreadsheets. 
In pandas, pivot tables are essentially just another way of performing grouped calculations. 
That is, the .pivot_table() method is just an alternative to .groupby().

In this exercise, you'll perform calculations using .pivot_table() to replicate the calculations 
you performed in the last lesson using .groupby().

"""

# Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)


# Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.
mean_med_sales_by_type = sales.pivot_table(
    values="weekly_sales", index="type", aggfunc=[np.mean, np.median])
# Print mean_med_sales_by_type
print(mean_med_sales_by_type)


# Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.

"""
Fill in missing values and sum values with pivot tables

The .pivot_table() method has several useful arguments, including fill_value and margins:

    fill_value replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course (Dealing with Missing Data in Python), but the simplest thing to do is to substitute a dummy value.
    margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: it gives the row and column totals of the pivot table contents.

"""

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins="sum"))
