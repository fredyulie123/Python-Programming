# Yifeng He Homework 8
# Code from Lab 4
# instance 1: Value Error & Zero Division Error
error = 'y'
while error == 'y':
    try:
        points_earned = float(input('How many points have you earned?\n>>')) # This line will throw an error if the user doesn't input a number.
        points_possible = float(input('How many points are currently possible?\n>>')) # This line will throw an error if the user doesn't input a number.

        percent = points_earned/points_possible*100 # # This line will throw an error if the user want to divide by zero.

        if percent >= 93:
            grade = 'A'
        elif percent >= 90 and points_earned < 93:
            grade = 'A-'
        elif percent >= 87:
            grade = 'B+' 
        else:
            grade = 'F'
        print('The student currently has', percent, '% with a letter grade of',grade)
        error = 'n'
    except ValueError:
        print('Cannot compute your total. You must submit numbers.')
    except ZeroDivisionError:
        print('You cannot divide by zero.')
        
# Code from Lab 7 Part D
# Instance 2: connection Error
try:    
    from bs4 import BeautifulSoup # If you doesn't download the package, it will throw an error
    from urllib.request import urlopen # If you doesn't download the package, it will throw an error

    url = 'http://www.musicpriceguide.com' # If you doesn't connect the internet, it will throw an error
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    title_tags = soup.find_all(title = True)
    for a in title_tags:
        print(a)
        
    for a in title_tags:
        print(a.get_text())
except ModuleNotFoundError:
    print('Please check if you download the package.')
except:
    print('Could not get the URL. Please check your internet connection.')
