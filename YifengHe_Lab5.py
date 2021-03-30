#Yifeng He Lab5
#Part A
def findLetterGrade(pointsEarned, pointsPossible = 100):
    percent = pointsEarned / pointsPossible * 100
    grade = 'Uknown'
    if percent >= 93:
        grade = 'A'
    elif percent >= 90:
        grade = 'A-'
    elif percent >= 87:
        grade = 'B+'
    elif percent >= 83:
        grade = 'B'
    elif percent >= 80:
        grade = 'B-'
    elif percent >= 77:
        grade = 'C+'
    elif percent >= 73:
        grade = 'C'
    elif percent >= 70:
        grade = 'C-'
    elif percent >= 67:
        grade = 'D+'
    elif percent >= 63:
        grade = 'D'
    elif percent >= 60:
        grade = 'D-'
    else:
        grade = 'F'
    return grade  # return grade --> to return output for next print
    
points = [96, 79, 88, 92, 62]
for p in points:
    letterGrade = findLetterGrade(p)
    s = 'The student with '+ str(p) + ' points received a ' + letterGrade
    print(s)
 
#Part B
def convertMoney(amount, fromInput, toInput = 'yen'):
    #Create list of possible answers
    yen = ['¥', 'y', 'yen','Yen','YEN']
    dollar = ['$', 'd', 'dollar', 'Dollar','DOLLAR']
    euro = ['€', 'e', 'euro','Euro','EURO']
    pound = ['£', 'p','pound','Pound','POUND']
    #Result if inputs are incorrect
    total = 'Invalid'
    #converstions from yen
    if fromInput in yen and toInput in dollar:
        total = amount * .009
    if fromInput in yen and toInput in euro:
        total = amount * .008
    if fromInput in yen and toInput in pound:
        total = amount * .0069
    #converstions from dollar
    if fromInput in dollar and toInput in yen:
        total = amount * 111.58
    if fromInput in dollar and toInput in euro:
        total = amount * .89
    if fromInput in dollar and toInput in pound:
        total = amount * .77
    #converstions from euro
    if fromInput in euro and toInput in yen:
        total = amount * 125.28
    if fromInput in euro and toInput in dollar:
        total = amount * 1.12
    if fromInput in euro and toInput in pound:
        total = amount * .86
    #converstions from pound
    if fromInput in pound and toInput in yen:
        total = amount * 144.82
    if fromInput in pound and toInput in dollar:
        total = amount * 1.3
    if fromInput in pound and toInput in euro:
        total = amount * 1.16
    #print the results
    print(amount, fromInput+'(s)', 'is worth', total, toInput+'(s)')
convertMoney(100, 'euro')
convertMoney(100, 'euro','pound')
