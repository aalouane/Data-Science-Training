'''
Which avocado size is most popular?

Avocados are increasingly popular and delicious in guacamole and on toast. 
The Hass Avocado Board keeps track of avocado supply and demand across the USA, including the sales of three different sizes of avocado. 
In this exercise, you'll use a bar plot to figure out which size is the most popular.

Bar plots are great for revealing relationships between categorical (size) and numeric (number sold) variables, but you'll often have to manipulate 
your data first in order to get the numbers you need for plotting
'''

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados)

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar", )

# Show the plot
plt.show()


'''
Changes in sales over time

Line plots are designed to visualize the relationship between two numeric variables, where each data values is connected to the next one. 
They are especially useful for visualizing the change in a number over time since each time point is naturally connected to the next time point. 
In this exercise, you'll visualize the change in avocado sales over three years.

'''

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")

# Show the plot
plt.show()


'''
Avocado supply and demand

Scatter plots are ideal for visualizing relationships between numerical variables. 
In this exercise, you'll compare the number of avocados sold to average price and see if they're at all related. 
If they're related, you may be able to use one number to predict the other.

matplotlib.pyplot has been imported as plt, pandas has been imported as pd, and avocados is available.
'''

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()


'''
Price of conventional vs. organic avocados

Creating multiple plots for different subsets of data allows you to compare groups. 
In this exercise, you'll create multiple histograms to compare the prices of conventional and organic avocados.
'''

# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend("conventional and organic")

# Show the plot
plt.show()

###############################################################
# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


'''
Finding missing values

Missing values are everywhere, and you don't want them interfering with your work. 
Some functions ignore missing data by default, but that's not always the behavior you might want. 
Some functions can't handle missing values at all, so these values need to be taken care of before you can use them. 
If you don't know where your missing values are, or if they exist, you could make mistakes in your analysis. In this exercise, 
you'll determine if there are missing values in the dataset, and if so, how many.
'''

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()


'''
Removing missing values

Now that you know there are some missing values in your DataFrame, you have a few options to deal with them. 
One way is to remove them from the dataset completely. In this exercise, you'll remove missing values by removing all rows that contain missing values.
'''
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())


'''
Replacing missing values

Another way of handling missing values is to replace them all with the same value. 
For numerical variables, one option is to replace values with 0— you'll do this here. 
However, when you replace missing values, you make assumptions about what a missing value means. 
In this case, you will assume that a missing number sold means that no sales for that avocado type were made that week. 
==> replacing missing values can affect the distribution of a variable.
'''

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

## => Notice how the distribution has changed shape after replacing missing values with zeros.


'''
List of dictionaries
'''
# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

'''
Dictionary of lists
'''
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)