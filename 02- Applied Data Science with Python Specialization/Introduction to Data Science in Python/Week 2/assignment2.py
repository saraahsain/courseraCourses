import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

#question 0
# What is the first country in df?
# This function should return a Series.
def answer_zero():
    return df.iloc[0]
answer_zero()

# Question 1
# Which country has won the most gold medals in summer games?
# This function should return a single string value.
def answer_one():
    return df.Gold.argmax()
answer_one()#'United States'

# Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
# This function should return a single string value.
def answer_two():
    return (df.Gold - df['Gold.1']).abs().argmax()
answer_two()#'United States'

# Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
# Only include countries that have won at least 1 gold in both summer and winter.
# This function should return a single string value.
def answer_three():
    incDF = df.where((df['Gold'] > 0) & (df['Gold.1'] > 0)).dropna()
    diff = (abs((incDF['Gold'] - incDF['Gold.1'])/incDF['Gold.2']))
    return diff.argmax()
answer_three()#'Bulgaria'

# Question 4
# Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
# This function should return a Series named Points of length 146
import numpy
def answer_four():
    #len(df) = 146 I checked
    points = numpy.zeros(len(df)) 
    points += df['Gold.2'] * 3
    points += df['Silver.2'] * 2
    points += df['Bronze.2']
    return pd.Series(points, index=df.index).astype(int)
answer_four()#Series of values

# Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# This function should return a single string value.
census_df = pd.read_csv('census.csv')
census_df.head()
def answer_five():
    states = census_df[census_df['SUMLEV'] == 50]
    return states.groupby('STNAME').count()['SUMLEV'].argmax()
answer_five()#'Texas'

# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
# This function should return a list of string values.
def answer_six():
    states = census_df[census_df['SUMLEV'] == 50]
    popCountries = states.sort_values('CENSUS2010POP', ascending=False).groupby('STNAME').head(3)
    return popCountries.groupby('STNAME').sum().sort_values('CENSUS2010POP', ascending=False).head(3).index.tolist()
answer_six()#['California', 'Texas', Illinois']

# Question 7
# Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
# This function should return a single string value.
def answer_seven():
    states = census_df[census_df['SUMLEV'] == 50][[6, 9, 10, 11, 12, 13, 14]]
    states["MaxDiff"] = abs(states.max(axis=1) - states.min(axis=1))
    largAbs =  states.sort_values(by=["MaxDiff"], ascending = False)
    return largAbs.iloc[0][0]
answer_seven()#'Harris County'

#Question 8
# In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
def answer_eight():
    region = census_df[(census_df['REGION'] == 1) | (census_df['REGION'] == 2)]
    startsWashington = region[region['CTYNAME'].str.startswith("Washington")]
    greater = startsWashington[startsWashington['POPESTIMATE2015'] > startsWashington['POPESTIMATE2014']]
    return greater[['STNAME', 'CTYNAME']]
answer_eight()#dataframe