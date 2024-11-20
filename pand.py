#pandas
import pandas as pd
import seaborn as sns

#1
#get a sample dataset

# makes a data frame containg the sns data set
df = sns.load_dataset('iris')
(df)

#2
#view summaries of it

# Prints out parts of the data frame
(df.head())
(df.tail())
(df.head(20))
(df.tail(20))

# Calcuates important info on the data frame
(df.describe()) #this just gives you a bunch just all of the data: calculates mean, count, max, min, 25%, etc

#3
#use groupby

# Makes a datagroup containing specific info
dg = df.groupby('species').mean() # the mean of each category of each species
dg = df.groupby('species').median() # the median of each category of each species
dg = df.groupby('species').max() # the max of each cateegory of each species
(dg)

#4
# show more or less rows
pd.set_option('display.max_rows', 20) # deterimines how many rows are printed when printing the data frame
(df)

#5
#sorting
df = df.sort_values(by = "sepal_width") #allows you to sort the data frame by chosen categories
print(df)
df1 = df.reset_index(drop = True)