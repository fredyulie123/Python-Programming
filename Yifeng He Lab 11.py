# Yifeng He Lab 11

import pandas as pd
import matplotlib.pyplot as pp

# Download datasets
"""
fileName = 'C:/Users/Yifeng He/Desktop/IO/'

import quandl
quandl.ApiConfig.api_key = 'BNy_ZPWsiEbwMz_BT8sL'

#userInput = input('Please enter the ticker symbol:\n>>')
#userInput = 'AAPL'  #First time Apple data
userInput = 'MSFT'  # Second time Microsoft
fileName = fileName+userInput+'.csv'
stockFound = 'n'
while stockFound == 'n':
    try:
        stockData = quandl.get('WIKI/'+userInput)
        print(stockData)
        stockFound = 'y'        
    except quandl.errors.quandl_error.NotFoundError:
        userInput = input('Could not find that ticker symbol. Please enter another ticker symbol:\n>>')        
    except:
        print('Could not connect to the data reader. Please check your internet connection.')
        stockFound = 'y'
stockData.to_csv(fileName, encoding = 'utf-8')
"""

# Pandas Practice
stock1FileName = 'C:/Users/Yifeng He/Desktop/IO/AAPL.csv'
stock2FileName = 'C:/Users/Yifeng He/Desktop/IO/MSFT.csv'

#read csv
stock1DF = pd.read_csv(stock1FileName, header = 0)
stock2DF = pd.read_csv(stock2FileName, header = 0)

print(stock1DF.info())

#cast datatype
stock1DF['Volume'] =stock1DF['Volume'].astype(int)
stock2DF['Volume'] =stock2DF['Volume'].astype(int)
stock1DF['Date'] = pd.to_datetime(stock1DF['Date'], format = '%Y-%m-%d')
stock2DF['Date'] = pd.to_datetime(stock2DF['Date'], format = '%Y-%m-%d')

#set index
stock1DF = stock1DF.set_index(['Date'])
stock2DF = stock2DF.set_index(['Date'])

#join
combinedDF = stock1DF.join(stock2DF, 'Date', 'outer', '_stock1', '_stock2')
#filter
print(combinedDF.loc['2000-01-01':'2000-02-01'][['Close_stock1', 'Close_stock2']])
#create new column
combinedDF['Difference'] = combinedDF['Close_stock1'] - combinedDF['Close_stock2']
#aggregate
combinedByYearDF = combinedDF.resample('Y').mean()

combinedByYearDF = combinedByYearDF[['Close_stock1', 'Close_stock2', 'Difference']]

#graphing
x = combinedByYearDF.index
y1 = combinedByYearDF['Close_stock1'].values
y2 = combinedByYearDF['Close_stock2'].values

pp.plot(x, y1)
pp.plot(x, y2)
#set label
pp.plot(x, y1, label = 'Apple')
pp.plot(x, y2, label = 'Microsoft')
#set legend title
pp.legend()
pp.xlabel('Date')
pp.ylabel('Price')
#set title
pp.title('Apple versus Microsoft')

pp.show()

