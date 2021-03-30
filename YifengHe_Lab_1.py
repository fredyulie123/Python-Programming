#Yifeng He Lab 1
#Part A
full_name = 'Shaw, Bernard'
comma_index = full_name.index(',')
last_name = full_name[:comma_index]
print(last_name)
first_name = full_name[comma_index+2:]
modified_full_name = first_name + ' ' + last_name
print(modified_full_name)

#Part B
original_bill = input('Please enter the bill amount:')
tip_input = input('Please enter the percent you would like to tip:')
print(original_bill, tip_input)
bill_float = float(original_bill)
tip_float = float(tip_input)
total = bill_float + (bill_float * tip_float * .01)
print('Your total bill with a', tip_input, 'percent tip is: $', total)

original_bill = input('Please enter the bill amount:\n>>')
tip_input = input('Please enter the percent you would like to tip:\n>>')
print(original_bill, tip_input)
bill_float = float(original_bill)
tip_float = float(tip_input)
total = bill_float + (bill_float * tip_float * .01)
print('Your total bill with a', tip_input, 'percent tip is:', '${0:,.2f}'.format(total))