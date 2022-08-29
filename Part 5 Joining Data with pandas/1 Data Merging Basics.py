'''
Your first inner join

You have been tasked with figuring out what the most popular types of fuel used in Chicago taxis are. 
To complete the analysis, you need to merge the taxi_owners and taxi_veh tables together on the vid column. 
You can then use the merged table along with the .value_counts() method to find the most common fuel_type.
'''

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

'''
Inner joins and number of rows returned

All of the merges you have studied to this point are called inner joins. 
It is necessary to understand that inner joins only return the rows with matching values in both tables. 
You will explore this further by reviewing the merge between the wards and census tables, then comparing it to merges of copies of these tables 
that are slightly altered, named wards_altered, and census_altered. The first row of the wards column has been changed in the altered tables. 
You will examine how this affects the merge between them. The tables have been loaded for you.
'''

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

# Print the first few rows of the wards_altered table to view the change 
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)

# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)


'''
One-to-many merge

A business may have one or multiple owners. In this exercise, you will continue to gain experience with one-to-many merges by merging a table 
of business owners, called biz_owners, to the licenses table. 
Recall from the video lesson, with a one-to-many relationship, a row in the left table may be repeated if it is related to multiple rows in the right table. 
In this lesson, you will explore this further by finding out what is the most common business owner title. (i.e., secretary, CEO, or vice president)
'''

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())


'''
Total riders in a month

Your goal is to find the total number of rides provided to passengers passing through the Wilson station (station_name == 'Wilson') 
when riding Chicago's public transportation system on weekdays (day_type == 'Weekday') in July (month == 7). 
Luckily, Chicago provides this detailed data, but it is in three different tables. You will work on merging these tables together to answer the question. 
This data is different from the business related data you have seen so far, but all the information you need to answer the question is provided.
'''

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == "Weekday") 
                   & (ridership_cal_stations['station_name'] == "Wilson"))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())


'''
Three table merge

To solidify the concept of a three DataFrame merge, practice another exercise. 
A reasonable extension of our review of Chicago business data would include looking at demographics information about the neighborhoods where 
the businesses are. A table with the median income by zip code has been provided to you. 
You will merge the licenses and wards tables with this new income-by-zip-code table called zip_demo.
'''

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip'). \
            			merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))


'''
One-to-many merge with multiple tables

In this exercise, assume that you are looking to start a business in the city of Chicago. 
Your perfect idea is to start a company that uses goats to mow the lawn for other businesses. 
However, you have to choose a location in the city to put your goat farm. You need a location with a great deal of space and relatively 
few businesses and people around to avoid complaints about the smell. You will need to merge three tables to help you choose your location. 
The land_use table has info on the percentage of vacant land by city ward. 
The census table has population by ward, and the licenses table lists businesses by ward.
'''
# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'], 
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'], 
                    ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

# ==> Using your skills, you were able to pull together information from different tables to see that the 7th ward would be a good place to build your goat farm!
