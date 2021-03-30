# Part A
journalfile_name = 'C:/Users/Yifeng He/Desktop/IO/DailyFile.txt'
m = input('Enter your daily log:\n>>')
with open (journalfile_name,'a', encoding='utf-8') as jf:
    jf.write(m)
    
# Part B
# Yifeng He Homework 6
originalfile_name = 'C:/Users/Yifeng He/Desktop/IO/tickerInfo.csv'
modifiedfile_name = 'C:/Users/Yifeng He/Desktop/IO/tickerInfoWithDelta.csv'

with open(originalfile_name, 'r', encoding='utf-8') as of, open(modifiedfile_name, 'a', encoding='utf-8') as mf:
    line = of.readline()
    line = of.readline()
    mf.write('Date, Close, Open, Delta, Direction\n')
    while line != '':
        line = line.replace('\n', '')
        line_list = line.split(',')
        Date = line_list[0]
        Close = line_list[1]
        Open = line_list[4]
        Delta = float(line_list[1])-float(line_list[4])
        if Delta > 0:
            Direction = 1
        else:
            Direction = 0
        line = of.readline()
        mf.write(Date + ',' + Close + ',' + Open + ',' + str(Delta) + ',' + str(Direction)+'\n')

        
    





    







