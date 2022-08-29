# Import cars data
import numpy as np
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Extract drives_right column as Series: dr

dr = cars["drives_right"]
print(dr)
# Use dr to subset cars:
sel = cars[dr]

# Print sel
print(sel)

#drives_right is a boolean column, so you'll have to extract it as a Series and then use this boolean Series to select observations from cars.

# ==========================================================================*
'''
Let's stick to the cars data some more. This time you want to find out which countries have a high cars per capita figure. 
In other words, in which countries do many people have a car, or maybe multiple cars.
'''
# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)
#

#===============================================================================
'''
Remember about np.logical_and(), np.logical_or() and np.logical_not(), the NumPy variants of the and, or and not operators? 
You can also use them on Pandas Series to do more advanced filtering operations.
'''

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Import numpy, you'll need this

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars["cars_per_cap"]
medium = cars[np.logical_and(cpc > 100, cpc < 500)]
# Print medium
print(medium)
