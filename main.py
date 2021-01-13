import pandas as pd
import re

# To read a .csv file using pandas library and print the data in the console...
#df = pd.read_csv('pokemon_data.csv')
#print(df)

#print(df.head(10))
#print(df.tail(5))
#print(df.head(1))

# To read a .xlsx file using pandas library and print the data in the console...
#df_excel = pd.read_excel('pokemon_data.xlsx')
#print(df_excel)

# To read a .txt file with a seperator or delimiter (Eg: tab) using pandas library and print the data in the console...
#df_text = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df_text.head(8))

# To read the column Header names...
#print(df.columns)

# To read all the column values (rows data) based on the name/header of the column...
#print(df.Name)
# or
#print(df['Name'])

# To read the specific column values (rows data) based on the name/header of the column...
#print(df['Name'][0:5])

# To read all the column values (rows data) based on multiple names/headers of the column...
#print(df[['Name', 'Type 2', 'Attack', 'Legendary']])
#print(df[['Type 2', 'Name', 'Legendary', 'Attack']])

# To read a specific row of data based on the index value of the row using iloc (integer location)...
#print(df.iloc[0])

# To read specific rows of data based on the index value of the row using iloc (integer location)...
#print(df.iloc[0:5])

# To read a specific data from a location based on row, column index number...
#print(df.iloc[4][1])
#print(df.iloc[4][2])
# or
#print(df.iloc[4,1])
#print(df.iloc[4,2])

# To read each row of data row by row using for loop...
#for index, row in df.iterrows():
#   print(index, row)
#   print(index, row['Name'])

# To filter based on a particular column value and read th data...
#print(df.loc[df['Type 1'] == "Grass"])
#print(df.loc[df['HP'] == 45])

# To display the statistical info like count, mean, std, min, max, 25%, 50%, 75% about the data....
#print(df.describe())

# To sort the data values in ascending order or descending based on columns/headers...
# Default sort is ascending order of the given column/header...
#print(df.sort_values('Name'))

# To sort the data values in the descending order based on a given column/header name...
#print(df.sort_values('Name', ascending=False))

# To sort the data values based on more than 1 column/header name...
#print(df.sort_values(['Name', 'HP']))
#print(df.sort_values(['Name', 'HP'], ascending=[1,1]))
#print(df.sort_values(['Name', 'HP'], ascending=[0,1]))
#print(df.sort_values(['Name', 'HP'], ascending=[1,0]))

# Change - To add a new column to the table (option 1)...
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df.head(5))
#print(df)

# Change - To delete/drop an existing column from the table...
#df = df.drop(columns = ['Total'])
#print(df)


# Change - To add a new column to the table using index position (option 2)...
# axis = 0 means we are adding the data values vertically...
# axis = 1 means we are adding the data values horizontally...
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)
#print(df.head(5))
#print(df)

# Change - To alter/change the display order, index positions of the columns
#cols = list(df.columns)                                 # list of list of data values
#df_1 = df[[cols[0]] + [cols[1]] + [cols[12]]]          # New Data Frame created only with 3 columns
#df_2 = df[cols[0:4] + [cols[-1]] + cols[4:12]]          # New Data Frame created with columns altered
#print(df_1, df_2)
#print(df_2[cols[4]])
#print(df_2.iloc[0][1])

# Writing modified data into .csv file along with index values
#df_1.to_csv('pokeman_data_1.csv')
#df_2.to_csv('pokeman_data_2.csv')

# Writing modified data into .csv file without index values
#df_1.to_csv('pokeman_data_1.csv', index=False)
#df_2.to_csv('pokeman_data_2.csv', index=False)

# Writing modified data into .xlsx file without index values
#df_1.to_excel('pokeman_data_1.xlsx', index=False)
#df_2.to_excel('pokeman_data_2.xlsx', index=False)

# Writing modified data into .txt file without index values
#df_1.to_csv('pokeman_data_1.txt', index=False, sep='\t')
#df_2.to_csv('pokeman_data_2.txt', index=False, sep='\t')

# Advanced Filters using conditions
#df_filter = df.loc[(df['Type 1'] == "Fire") & (df['Type 2'] == "Fairy") & (df['HP'] > 65)]
#df_filter = df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison") & (df['HP'] > 65)]
#df_filter_1 = df.loc[(df['Type 1'] == "Fire") | (df['Type 2'] == "Fairy")]
#print(df_filter)
#print(df_filter_1)

# To have new index values in the filtered data frame; instead of having index values copied from the original data frame...
#df_filter.reset_index(drop=True, inplace=True)
#print(df_filter)

# Advanced Filer - To filter data based on a given sub-string...
#print(df.loc[df['Type 1'].str.contains('Grass')])
#print(df.loc[df['Name'].str.contains('Diancie')])
#print(df.loc[df['Name'].str.contains('Mega')])


# Advanced Filer - To not to filter data based on a given sub-string using not symbol as "~"...
#print(df.loc[~df['Name'].str.contains('Mega')])


# Advanced Filer using Regular Expressions which are case sensitive...
# We need to "import re" library
#print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])

# Advanced Filer using Regular Expressions which are case in-sensitive...
# We need to "import re" library
#print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
#print(df.loc[df['Type 1'].str.contains('wATer|BUG', flags=re.I, regex=True)])


# Advanced Filter using Regular Expressions to filter data that contains/starts with a given sub-string as case insensitive...
#print(df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)])

# Advanced Filter using Regular Expressions to filter data that only starts with a given sub-string as case insensitive...
#print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

# Replacing the existing values for one or more columns using given condition...
#print(df.replace(["Fire"], "Flames"))
#print(df.replace(["Flames"], "Fire"))


# Grouping Data based on statistical functions like mean for analysis purposes...
#print(df)
#print(df.describe())
#print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))
#print(df.groupby(df['Type 1']).mean().sort_values('Defense', ascending=False))
#print(df.groupby(df['Type 1']).sum())
#print(df.groupby(df['Type 1']).count())

# Adding a new column and checking the count of 'Type 1' column values in the data set...
#df['Count'] = 1
#print(df.groupby(df['Type 1']).count()['Count'])
# or
#print(df.groupby(['Type 1']).count()['Count'])

# Grouping Data based on multiple columns...
#df['Count'] = 1
#print(df.groupby(['Type 1', 'Type 2']).count()['Count'])

# To load data rows in small chunks while working with large-sized data sets and avoid system memory problems in computer...
'''
for df in pd.read_csv('pokeman_data.csv', chunksize=5):
    print(df)
'''