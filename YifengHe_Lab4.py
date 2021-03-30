#YifengHe_Lab_4
#Part A
commenters = ['22.8.11.3.4', '12.0.13.3.4.11.0', '6.0.13.3.7.8', '19.20.17.8.13.6', '10.8.13.6',
'21.14.11.19.0.8.17.4']
localVisits = ['7.0.11.4','19.20.1.12.0.13', '12.0.13.3.4.11.0', '6.0.13.3.7.8', '10.8.13.6',
'15.0.8.13.4']
for customerID in commenters:
    if customerID in localVisits:
        print(customerID)
        
#Part B
fibList = [0, 1]
num1 = 0
num2 = 1
maxNumber = int(input('How many numbers would you like to see?\n>>'))
while len(fibList) < maxNumber and num2 < 1000000000000:
    newNumber = num1 + num2
    fibList.append(newNumber)
    newNumber = num1 + num2
    num1 = num2
    num2 = newNumber
    
if num2 > 1000000000000:
    print('Calculation ended to prevent memory overload')
    print(fibList)
else:
    print('Voilà, the first', maxNumber, 'numbers in the Fibonacci Sequence')
    print(fibList)
   