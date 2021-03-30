#YifengHe_Homework4
#Part A
speedsKPH = [60, 70, 80, 90, 100, 110, 120, 130]
print('KPH','MPH')
for i in speedsKPH:
    speedsMPH = i * 0.6214
    print(i, round(speedsMPH,3))
    
#Part B
secret_word = 'ambiguous'
times = 0
while times < 7:
    times += 1
    guess_letter = input('Guess a letter:\n>>')
    while len(guess_letter) != 1:
        guess_letter = input('Guess a letter:\n>>')
    if guess_letter in secret_word:
        print('Yes,', guess_letter, 'is in the word.')
    else:
        print('No,', guess_letter, 'is NOT in the word.')
        
guess_word = input('Can you guess the word?\n>>')
if guess_word == secret_word:
    print('Winner Winner, Chicken Dinner! That is correct!')
else:
    print('No, the word was', secret_word)

#Part C & Extra Challange
password = 'Coconut827'
attempt_times = 3
access_try = input('Please enter the password:\n>>')
while attempt_times >=1:
    attempt_times-= 1
    if access_try == password:
        print('Access granted')
        break
    else:
        access_try = input('That is incorrect, please try again ('+ str(attempt_times) + ' attempts left):\n>>')
else:
    print('Access denied')
