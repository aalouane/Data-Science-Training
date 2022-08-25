# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from data import *

year = []
pop = []
# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# --------------- Exemple 
# Print the last item of gdp_cap and life_exp
print(gdp_cap)
print(life_exp)

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
import matplotlib.pyplot as plt

# Display the plot
plt.plot(gdp_cap, life_exp)
plt.show()

#----------------------------------------------------
# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()

# from the teste :  There's no clear relationship between population and life expectancy, which makes perfect sense.
#===========================================================
# Build a histogram (1)

# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

'''
In the previous exercise, you didn't specify the number of bins. By default, Python sets the number of bins to 10 in that case. 
The number of bins is pretty important. Too few bins will oversimplify reality and won't show you the details. Too many bins will overcomplicate reality and won't show the bigger picture.
To control the number of bins to divide your data in, you can set the bins argument.
'''

plt.hist(life_exp, bins=20)

# Show and clean up again
plt.show()
plt.clf()

'''
Let's do a similar comparison. life_exp contains life expectancy data for different countries in 2007. 
You also have access to a second list now, life_exp1950, containing similar data for 1950. Can you make a histogram for both datasets?
'''

'''
Choose the right plot (1)

You're a professor teaching Data Science with Python, and you want to visually assess if the grades on your exam follow a particular distribution. Which plot do you use?
    Incorrect. A line plot won't give you a very clear visual on the distribution of the values in a list.
    Incorrect. Although a scatter plot can give you an idea, it's not the best option.
    Histogram

You're a professor in Data Analytics with Python, and you want to visually assess if longer answers on exam questions lead to higher grades. Which plot do you use?
    Making a line plot of this data will cause the lines to be all over the place. Do you still remember how the gdp_cap versus life_exp plot wasn't a good fit for the line plot?
    Scatter
'''
#=========================================================================
'''# Customization:
Many option:
    Different plot types
    many Customization
Choice Depends on 
    Data
    Story you want to tell
'''

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)

#  Let's change this. Wouldn't it be nice if the size of the dots corresponds to the population?
'''
To accomplish this, there is a list pop loaded in your workspace. It contains population numbers for each country expressed in millions. 
You can see that this list is added to the scatter method, as the argument s, for size.
'''
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

# ---------------------- Colors ---------------------------------
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c=col, alpha=0.8)
# alpha : opacity

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()