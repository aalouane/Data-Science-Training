# Definition of dictionary
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for k, v in europe.items():
    print("the capital of "+k+" is "+v)


# =======================================================
# Import numpy as np

# For loop over np_height
for x in np.nditer(np_height):
    print(str(x)+" inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)

#==========================================================
# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(row['country'])

#------------------------------------------------------------

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab+": "+str(row['cars_per_cap']))

# =================================================================
'''
In the video, Hugo showed you how to add the length of the country names of the brics DataFrame in a new column:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

but it's not the perfect way
'''

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)

# ========================================================================
'''
Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to understand, but not very efficient. On every iteration, you're creating a new Pandas Series.

If you want to add a column to a DataFrame by calling a function on another column, the iterrows() method in combination with a for loop is not the preferred way to go. Instead, you'll want to use apply().

Compare the iterrows() version with the apply() version to get the same result in the brics DataFrame:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

brics["name_length"] = brics["country"].apply(len)

'''
# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)

#===========================================================================================

# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)


# Show the plot
plt.show()
#=================================================================================================
'''
Visualize all walks

all_walks is a list of lists: every sub-list represents a single random walk. If you convert this list of lists to a NumPy array, you can start making interesting plots! matplotlib.pyplot is already imported as plt.

The nested for loop is already coded for you - don't worry about it. For now, focus on the code that comes after this for loop.
'''
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

#=====================================================================
# for Plot the distribution : we use a histogramme : plt.hist(np_array)
# the last row of two dimensional array : plt[-1,:]
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

'''
Calculate the odds

The histogram of the previous exercise was created from a NumPy array ends, that contains 500 integers. Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 500, the total number of simulations.

Well then, what's the estimated chance that you'll reach at least 60 steps high if you play this Empire State Building game? The ends array is everything you need; it's available in your Python session so you can make calculations in the IPython Shell.
'''

# Congratulations!

# You’ve completed Intermediate Python.
