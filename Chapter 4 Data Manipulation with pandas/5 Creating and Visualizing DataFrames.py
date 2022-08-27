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