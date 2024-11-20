import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import os

os.system('cls')

#steps of data science
#1 get data
#2 view data
#3 plot data
#4 simplify data
#5 manipulate data

#1 get data
#Get our data with chat gpt

#create a ticker object for bitcoin
btc = yf.Ticker("BTC-USD")

#get historical market data are you a dictionary
df = btc.history(period = "1mo")

#2 view Data
(df)
(df.head())
pd.set_option('display.max_columns', None) # sets pandas max columns to none
pd.set_option('display.max_rows', 5) # sets pandas max rows to none
(df)
(df.tail())
df = df.reset_index(drop = False)

'''
#3
#Plot Data
df.plot(x = 'Date', y = 'Close')
plt.show()
'''


#4
#Simplfy data
print(df.columns)
print(df)
df = df[['Date', 'Close', 'Low']]
print(df)

(df.head())
df = df.rename(columns = {'Date': 'date', 'Close': 'close'})
(df.head())

#5
#Manipulate Data
df['ret'] = df.close.shift(-1)/df.close - 1
(df)
(df.tail())

(type(df))