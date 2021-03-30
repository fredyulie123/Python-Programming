#Yifeng He Lab 2
print('Welcome to the Grader. Please add all the points you currently have and all the points currently possible.')
ready = input('Are you ready?\n>>')
affirmative = ['Yes', 'Y', 'yes', 'y', 'yup', 'Yup', 'Sure', 'sure']
if ready in affirmative:
    print('Ok, let\'s get started')
else:
    print('Please restart the program when you\'re ready. ')
 
points_earned = float(input('How many points have you earned?\n>>'))
points_possible = float(input('How many points are currently possible?\n>>'))
percent = points_earned/points_possible*100

if percent >= 93:
    grade = 'A'
elif percent >= 90 and points_earned < 93:
    grade = 'A-'
elif percent >= 87:
    grade = 'B+' 
else:
    grade = 'F'
print('The student currently has', percent, '% with a letter grade of',grade)

#Extra challenge
print('Welcome to the Grader. Please add all the points you currently have and all the points currently possible.')
ready = input('Are you ready?\n>>')
affirmative = ['Yes', 'Y', 'yes', 'y', 'yup', 'Yup', 'Sure', 'sure']
if ready in affirmative:
    print('Ok, let\'s get started')
else:
    print('Please restart the program when you\'re ready. ')
Items = ['Lab_1','Lab_2','Lab_3','Lab_4','Homework_1','Homework_2','Homework_3','Homework_4','Exam_1','Exam_2']
earned = []
possible = []
for i in Items:
    points_earned = input('Please enter your score on ' + i + '. When done, press d:\n>>')
    if points_earned == 'd':
        continue
    else:
        points_possible = input('How many points on '+ i +' are currently possible?\n>>')
        if points_possible >= points_earned:
            
            earned.append(float(points_earned))
            possible.append(float(points_possible))
        else:
            continue
percent = sum(earned)/sum(possible)*100
if percent >= 93:
    grade = 'A'
elif percent >= 90 and points_earned < 93:
    grade = 'A-'
elif percent >= 87:
    grade = 'B+' 
else:
    grade = 'F'
print('The student currently has', percent, '% with a letter grade of',grade)
    
        
