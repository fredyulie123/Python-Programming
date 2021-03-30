#YifengHe_LAB_3
#Part A
urls = ['https://www.yelp.com/biz/levain-bakery-new-york']
nextPageStart = 20
i = 0
while i < 5:
    i += 1
    nextPage = 'https://www.yelp.com/biz/levain-bakery-new-york?start=' + str(nextPageStart)
    nextPageStart += 20
    urls.append(nextPage)
print(urls)

#Part B
print('Welcome to the palindrome finder!')
attempt = str(input('Please enter a word or phrase to test:\n>>'))
cleanedAttempt = attempt.replace('.', '').replace('!', '').replace(',', '').replace(':', '').replace(';',
'').replace('?', '').replace(' ', '')
reverseAttempt = cleanedAttempt[::-1]
allPalindromes = []
if reverseAttempt.lower() == cleanedAttempt.lower():
    print('Yes,', attempt, 'is a palidrome!')
    allPalindromes.append(attempt)
else:
    print('No, it does not seem', attempt, 'is a palindrome')
while attempt != '':
    attempt = input('Enter another word or phrase to test (or Enter to exit):\n>>')
    cleanedAttempt = attempt.replace('.', '').replace('!', '').replace(',', '').replace(':', '').replace(';',
    '').replace('?', '').replace(' ', '')
    reverseAttempt = cleanedAttempt[::-1]
    if reverseAttempt.lower() == cleanedAttempt.lower():
        print('Yes,', attempt, 'is a palidrome!')
        allPalindromes.append(attempt)
    else:
        print('No, it does not seem', attempt, 'is a palindrome')
print('Thank you for using the palindrome finder. You found the following palindromes:')
for p in allPalindromes:
    print(p)
 

 
# This code is contributed by Sachin Bisht