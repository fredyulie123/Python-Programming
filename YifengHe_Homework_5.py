#Yifeng He Homework 5
#Part A
def find_fibonacci(n):
    i = 0
    number_A = 0
    number_B = 1
    while i < n:
        next_number = number_A + number_B
        number_A = number_B
        number_B = next_number
        i += 1
    return number_A

response = int(input('Which number would you like to find?:\n>>'))
result = find_fibonacci(response)
print(result)

#Part B
def birthday_song(user_name):
    h = print('Happy Birthday to you,\n'
          'Happy Birthday to you,\n'
          'Happy Birthday, dear', user_name, '\n'
          'Happy Birthday to you!')
    return h
     
response = input('What is your name?\n>>')
result = birthday_song(response)


#Part C
def future_value(p, r, t, n = 365):
    p_float = float(p.replace('$', '').replace(',', ''))
    r_float = float(r.replace('%', ''))*.01
    a = p_float*(1 + r_float/n)**(n*t)
    return a

loan = [['$5,000.00','7.9%',5],['$12,000','3.2%',10],['$1,700,000','4.8%',30,4]]
for m in loan:
    if len(m) == 4 :
        fv = future_value(m[0],m[1],m[2],m[3])
    else:
        fv = future_value(m[0],m[1],m[2])
    print(fv)

    
    
    
    
