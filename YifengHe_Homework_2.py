#YifengHe_Homework2
#Part A
short_acting = ['Humulin', 'Novolin']
rapid_acting = ['NovoLog', 'FlexPen', 'Fiasp', 'Apidra']
prescribed = input('What medication has the patient been prescribed \n>>')
if prescribed in short_acting and rapid_acting:
    print('The patient is a diabetic.')
else:
    print('The patient is not a diabetic.')
 
#Part B
maximum_amount = 500
willing_payable = float(input('How much are you asking? \n>>'))
if willing_payable <= maximum_amount:
    print('Ok, I would like to purchase it.')
else:
    print('Sorry, that price is too high for me.')
    
#Part C
print('Welcome to the currency calculator!')
currency_type =['d','y','e','p']
amount_num = float(input('Enter the amount: \n>>'))
original_currency = input('Enter the original currency: \n>>')
new_currency = input('Enter the new currency: \n>>')
if original_currency == currency_type[0] and new_currency == currency_type[1]:
    new_num = amount_num *109.84
    print ('{0:,.2f}'.format(amount_num),'Dollar(s) is worth','{0:,.2f}'.format(new_num), 'Yen(s).')
elif original_currency == currency_type[0] and new_currency == currency_type[2]:
    new_num = amount_num *0.92
    print ('{0:,.2f}'.format(amount_num),'Dollar(s) is worth','{0:,.2f}'.format(new_num), 'Euro(s).')
elif original_currency == currency_type[0] and new_currency == currency_type[3]:
    new_num = amount_num *0.77
    print ('{0:,.2f}'.format(amount_num),'Dollar(s) is worth','{0:,.2f}'.format(new_num), 'Pound(s).')
elif original_currency == currency_type[1] and new_currency == currency_type[0]:
    new_num = amount_num *0.0091
    print ('{0:,.2f}'.format(amount_num),'Yen(s) is worth','{0:,.2f}'.format(new_num), 'Dollar(s).')    
elif original_currency == currency_type[1] and new_currency == currency_type[2]:
    new_num = amount_num *0.0083
    print ('{0:,.2f}'.format(amount_num),'Yen(s) is worth','{0:,.2f}'.format(new_num), 'Euro(s).')     
elif original_currency == currency_type[1] and new_currency == currency_type[3]:
    new_num = amount_num *0.0070
    print ('{0:,.2f}'.format(amount_num),'Yen(s) is worth','{0:,.2f}'.format(new_num), 'Pound(s).')
elif original_currency == currency_type[2] and new_currency == currency_type[0]:
    new_num = amount_num *1.09
    print ('{0:,.2f}'.format(amount_num),'Euro(s) is worth','{0:,.2f}'.format(new_num), 'Dollar(s).')
elif original_currency == currency_type[2] and new_currency == currency_type[1]:
    new_num = amount_num *119.86
    print ('{0:,.2f}'.format(amount_num),'Euro(s) is worth','{0:,.2f}'.format(new_num), 'Yen(s).')
elif original_currency == currency_type[2] and new_currency == currency_type[3]:
    new_num = amount_num *0.84
    print ('{0:,.2f}'.format(amount_num),'Euro(s) is worth','{0:,.2f}'.format(new_num), 'Pound(s).')
elif original_currency == currency_type[3] and new_currency == currency_type[0]:
    new_num = amount_num *1.30
    print ('{0:,.2f}'.format(amount_num),'Pound(s) is worth','{0:,.2f}'.format(new_num), 'Dollar(s).')
elif original_currency == currency_type[3] and new_currency == currency_type[1]:
    new_num = amount_num *142.28
    print ('{0:,.2f}'.format(amount_num),'Pound(s) is worth','{0:,.2f}'.format(new_num), 'Yen(s).')
elif original_currency == currency_type[3] and new_currency == currency_type[2]:
    new_num = amount_num *1.19
    print ('{0:,.2f}'.format(amount_num),'Pound(s) is worth','{0:,.2f}'.format(new_num), 'Euro(s).')
else:
    print('sorry, you can\'t calculate it.')
    
#Extra Challenge
print('Welcome to the currency calculator!')
dollar = ['dollar','Dollar','$','DOLLAR']
euro = ['euro','Euro','€','EURO']
yen = ['yen','Yen','¥','YEN']
pound = ['pound','Pound','£','POUND']
amount_num = float(input('Enter the amount: \n>>'))
original_currency = input('Enter the original currency: \n>>')
new_currency = input('Enter the new currency: \n>>')
if original_currency in dollar and new_currency in yen:
    new_num = amount_num *109.84
    print ('{0:,.2f}'.format(amount_num),'Dollar(s) is worth','{0:,.2f}'.format(new_num), 'Yen(s).')
elif original_currency in dollar and new_currency in euro:
    new_num = amount_num *0.92
    print ('{0:,.2f}'.format(amount_num),'Dollar(s) is worth','{0:,.2f}'.format(new_num), 'Euro(s).')
elif original_currency in dollar and new_currency in pound:
    new_num = amount_num *0.77
    print ('{0:,.2f}'.format(amount_num),'Dollar(s) is worth','{0:,.2f}'.format(new_num), 'Pound(s).')
elif original_currency in yen and new_currency in dollar:
    new_num = amount_num *0.0091
    print ('{0:,.2f}'.format(amount_num),'Yen(s) is worth','{0:,.2f}'.format(new_num), 'Dollar(s).')    
elif original_currency in yen and new_currency in euro:
    new_num = amount_num *0.0083
    print ('{0:,.2f}'.format(amount_num),'Yen(s) is worth','{0:,.2f}'.format(new_num), 'Euro(s).')     
elif original_currency in yen and new_currency in pound:
    new_num = amount_num *0.0070
    print ('{0:,.2f}'.format(amount_num),'Yen(s) is worth','{0:,.2f}'.format(new_num), 'Pound(s).')
elif original_currency in euro and new_currency in dollar:
    new_num = amount_num *1.09
    print ('{0:,.2f}'.format(amount_num),'Euro(s) is worth','{0:,.2f}'.format(new_num), 'Dollar(s).')
elif original_currency in euro and new_currency in yen:
    new_num = amount_num *119.86
    print ('{0:,.2f}'.format(amount_num),'Euro(s) is worth','{0:,.2f}'.format(new_num), 'Yen(s).')
elif original_currency in euro and new_currency in pound:
    new_num = amount_num *0.84
    print ('{0:,.2f}'.format(amount_num),'Euro(s) is worth','{0:,.2f}'.format(new_num), 'Pound(s).')
elif original_currency in pound and new_currency in dollar:
    new_num = amount_num *1.30
    print ('{0:,.2f}'.format(amount_num),'Pound(s) is worth','{0:,.2f}'.format(new_num), 'Dollar(s).')
elif original_currency in pound and new_currency in yen:
    new_num = amount_num *142.28
    print ('{0:,.2f}'.format(amount_num),'Pound(s) is worth','{0:,.2f}'.format(new_num), 'Yen(s).')
elif original_currency in pound and new_currency in euro:
    new_num = amount_num *1.19
    print ('{0:,.2f}'.format(amount_num),'Pound(s) is worth','{0:,.2f}'.format(new_num), 'Euro(s).')
else:
    print('sorry, you can\'t calculate it.')
