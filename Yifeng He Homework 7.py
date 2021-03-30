#Yifeng He Homework 7
#Part A
customer = {'name': 'Orwell', 'address':'4 Church St', 'age':'46'}
print (customer['address'])
customer['birthday'] = '25 June'
customer['name'] = 'Orwell, George'
print(customer)
#Part A Extra Challenge
customer_e = {1:{'name': 'Orwell', 'address':'4 Church St', 'age':'46'}
            , 2:{'name': 'Cicero', 'address':'11 Carmine St', 'age':'63'}}
print(customer_e[1]['address'])
customer_e[1]['birthday'] = '25 June'
customer_e[1]['name'] = 'Orwell, George'
print(customer_e)

#Part B
phonebook = {
            'Euclid': {'number':'212.479.2851'}
            , 'Pythagoras': {'number':'212.479.4653'}
            , 'Avicenna': {'number':'212.892.1234'}
            , 'Descartes': {'number':'917.372.1650'}
            }
m = phonebook.get('Newton', 'Name not found')
print (m)
if m == 'Name not found':
    phonebook['Newton'] = {'number':'917.364.1727'}
phonebook['Avicenna'] ['number']= '212.472.1037'
del phonebook['Descartes']
for p in phonebook:
    print(p, phonebook[p]['number'])
    
#Part B Extra Challenge
for p in phonebook:
    phonebook[p]['areaCode'] = phonebook[p] ['number'][0:3]
print (phonebook)
s = input('The number which you want to search:\n>>')
for p in phonebook:
    if phonebook[p]['number'] == s:
        print ('The name associated with', s, 'is:', p)
        

#Part C
phonebook1 = {
            'Euclid': {'number':'212.479.2851'}
            , 'Pythagoras': {'number':'212.479.4653'}
            , 'Avicenna': {'number':'212.472.1037'}
            , 'Newton': {'number': '917.364.1727'}
            }
import pandas as pd
phonebook1_df = pd.DataFrame(phonebook1)
phonebook1_df = phonebook1_df.transpose()
print(phonebook1_df)

    


    
    