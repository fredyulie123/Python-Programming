#Homework 1
#Part A
pagination = 'Page 1 of 12'
total_pageNum = pagination[pagination.index('12'):]
Page_Num = int(total_pageNum)
print (Page_Num)

#Part B
runner1 = 300.25 #Finish time in Minutes
runner2 = 260.75
runner3 = 315.75
runner4 = 245.25
average = (runner1+runner2+runner3+runner4)/4
print('Average:', average)
variance = (((runner1-average)**2+(runner2-average)**2+(runner3-average)**2+
(runner4-average)**2)/4)
print('Variance:', variance)

#Part C
principal_num = input('Please enter principal:\n>>')
annual_rate = input('Please enter annual interest rate:\n>>')
num_year = input('Please enter the term in years:\n>>')
term_num = input('Please enter number of times the interest will compound per year:\n>>')
print(principal_num, annual_rate, num_year, term_num)
pv_float = float(principal_num)
r_float = float(annual_rate)
y_float = float(num_year)
n_float = float(term_num)
future_value = float(pv_float*(1+r_float/n_float/100)**(y_float*n_float))
print("In", y_float, "years,","at the interest rate of", r_float, "% compounded", n_float, "times per year, the initial amount of $", '{0:,.2f}'.format(pv_float), 'will be worth ', '${0:,.2f}'.format(future_value), ".")


#Extra Challenge
principal_num = input('Please enter principal: ')
annual_rate = input('Please enter annual interest rate: ')
num_year = input('Please enter the term in years: ')
term_num = input('Please enter number of times the interest will compound per year: ')
print(principal_num, annual_rate, num_year, term_num)
pv_float = float(principal_num)
r_float = float(annual_rate)
y_float = float(num_year)
n_float = float(term_num)
future_value = float(pv_float*(1+r_float/n_float/100)**(y_float*n_float))
interest_num = float(future_value-pv_float)
print("In", y_float, "years,","at the interest rate of", r_float, "% compounded", n_float, "times per year, the initial amount of $", '{0:,.2f}'.format(pv_float), 'will be worth ', '${0:,.2f}'.format(future_value), ".", '${0:,.2f}'.format(interest_num), "will be paid in interest.")
