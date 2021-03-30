#Homework_3_Yifeng_He
#Part A
a = 'v'
response = int(input('How many \'waves\' you would like to print?\n>>'))
i = 1
while i < response:
    i+=1
    a+='v'
print(a)

#Part B
names = ['Smith, Tommie', 'Carlos, John', 'Normen, Peter']
for i in names:
    comma_index = i.index(',')
    last_name = i[:comma_index]
    first_name = i[comma_index+2:]
    modified_full_name = first_name + ' ' + last_name
    print(modified_full_name)
    
#Part C
min_price = 15
deal_price = min_price
offer = float(input('How much will you pay?\n>>'))
while offer < deal_price:
    deal_price +=2
    offer = float(input('Nope! Try offering more:\n>>'))
print('It\'s a deal! The price is ',offer)
#Extra Challenge Part C
over_paid = offer - min_price
print('You over paid by $', over_paid, ', I was originally willing to sell for $', min_price)

#Extra Challenge
print('Welcome to the Cows and Bulls game!')
power_ball = 6237
a = str(power_ball)
times = 0
cows = 0
bulls = 0
while cows < 4:
    cows = 0
    bulls = 0
    times+=1
    guess_num = input('Please input a 4-digit number:\n>>')
    while len(guess_num) != 4:
        guess_num = input('Please input another 4-digit number:\n>>')
    for i in range(len(guess_num)):
        if guess_num[i] == a[i]:
            cows += 1            
        else:
            if guess_num[i] in a and guess_num[i] != a[i]:
                bulls += 1
            else:
                continue
    print('You get', cows, 'cows,' ,bulls, 'bulls.')        
print('Well done! The correct number is:', power_ball, 'It only took', times, 'attempts.')
    