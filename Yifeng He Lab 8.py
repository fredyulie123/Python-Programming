# Yifeng He Lab 8
location_dic = {'Bothell': [12, 18, 34, 44, 42, 22]
                , 'Portland' : [11, 19, 22, 0, 0, 0]
                , 'Salem' : [19, 12, 18, 26, 31, 12]
                , 'Sunset' : [7, 12, 14, 17, 20, 15]
                , 'Forest Grove' : [13, 15, 22, 29, 41, 33]
                , 'McMinnville' : [21, 35, 66, 79, 77, 44]
                , 'Vancouver' : [11, 22, 21, 20, 19, 11]
                , 'Bend' : [44, 98, 102, 133, 130, 110]
                , 'Centralia' : [66, 12, 18, 22, 33, 22]
              }
location_dic['Tigard']=[14, 19, 19, 29, 33, 11]
location_dic['Portland']=[11, 19, 22, 31, 37, 16]

location_total_dic = {}
for location in location_dic:
    total = sum(location_dic[location])
    location_total_dic[location]=total
    
for t in location_total_dic:
    print(t, location_total_dic[t])
    
print(min(location_total_dic.values()))

lowest = min(location_total_dic.values())

for t in location_total_dic:
    if location_total_dic[t] == lowest:
        print(t, 'had the fewest clicks with', lowest)
        del location_dic[t]

import pandas as pd
location_df = pd.DataFrame(location_dic)
print(location_df)

location_df = location_df.transpose()
print(location_df)

print(location_df.sum())
