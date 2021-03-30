#Yifeng He Lab 9
#Part A
fileName = 'C:/Users/michael.deamer/Desktop/Python IO/StockInfo.txt'
import quandl
quandl.ApiConfig.api_key = 'BNy_ZPWsiEbwMz_BT8sL'
# stockData = quandl.get('WIKI/MACK')
# print(stockData)

#userInput = input('Please enter the ticker symbol:\n>>')  #Part A step 13
userInput = 'MACK'
stockFound = 'n'
while stockFound == 'n':    
    try:
        stockData = quandl.get('WIKI/'+ userInput)
        stockFound = 'y'
    except quandl.errors.quandl_error.NotFoundError:
        userInput = input('Could not find that ticker symbol. Please enter another ticker symbol:\n>>')
    except:
        print('Could not connect to Quandl. Please check your internet connection.')
        stockFound = 'y'


#Part B
#file = open(fileName, 'w', encoding ='utf-8')
#file.write(stockData.to_string())
#file.close()
try:
    file = open(fileName, 'a', encoding ='utf-8')
    file.write(stockData.to_string())
except NameError:
    print('Error loading data')
except PermissionError:
    print('Please close any program using MackStock.txt and try again')
finally:
    try:
        file.close()
    except:
        pass
    

