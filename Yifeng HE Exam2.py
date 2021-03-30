# Exam 2 Yifeng He

# Trip Planner
planner_name = 'C:/Users/Yifeng He/Desktop/graduated/2nd graduate semester/Python/Trip Planner.txt' # create file path
print('Welcome to the road trip planner!')

## recording trip details
allstation = [] # prepare for append trip details
gasprice = 3 # gas per gallon price
mpg = 35 # mile per gallon
total_cost = 0 
ready = input('Are you ready for make a trip plan (Enter \'n\' for no)?\n>>')
affirmative = ['Yes', 'Y', 'yes', 'y', 'yup', 'Yup', 'Sure', 'sure']
if ready in affirmative:

# ask for starting location
    start_loc = str(input('Please enter your starting location:\n>>'))
    origin_loc = start_loc # departure place

# ask for destination location
    desti_loc = str(input('From '+ start_loc + ', where will you travel?\n>>'))

# ask for distance
    distance = float(input('How far away is ' + desti_loc + ' from ' + start_loc +'?\n>>'))

# calculate the cost
    cost = (distance/mpg)*gasprice
    total_cost = total_cost + cost

# append trip detail
    allstation.append([start_loc, desti_loc, round(distance,2), round(cost,2)])

# ask if have another plan
    ready = input('Will you be travelling beyond ' + desti_loc + ' (Enter \'n\' for no)?\n>>')

# ask for another plan
    while ready in affirmative:
        start_loc = desti_loc
        desti_loc = str(input('From '+ start_loc + ', where will you travel?\n>>'))
        distance = float(input('How far away is ' + desti_loc + ' from ' + start_loc +'?\n>>'))
        cost = (distance/mpg)*gasprice
        total_cost = total_cost + cost
# append trip detail
        allstation.append([start_loc, desti_loc, round(distance,2), round(cost,2)])
        ready = input('Will you be travelling beyond ' + desti_loc + ' (Enter \'n\' for no)?\n>>')
    final_loc = desti_loc # destination place
    
#write down overview
    overview = 'Your entire trip from ' + origin_loc + ' to ' + final_loc + ' will cost $' + str(round(total_cost,2)) + '\n'
    with open (planner_name,'w', encoding='utf-8') as pn:
        pn.write(overview)
else:
    print('Please restart the trip planner when you\'re ready. ')

# write down details
for p in range(0,len(allstation)):
    start_station = allstation[p][0]
    desti_station = allstation[p][1]
    per_cost = allstation[p][3]
    detail = start_station + ' to ' + desti_station + ' will cost $' + str(round(per_cost,2)) + '\n'
    with open (planner_name,'a', encoding='utf-8') as pn:
        pn.write(detail)
    


    
