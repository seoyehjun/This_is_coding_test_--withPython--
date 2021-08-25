#3:47 # 4:18 ---> 31min
def str_to_num(list):
    for var in range(len(list)):
        if list[var] == 'R':
            list[var] = (0,1)
        elif list[var] == 'L':
            list[var]= (0,-1)
        elif list[var] == 'U':
            list[var] =  (-1,0)
        elif list[var] == 'D':
            list[var] =  (1,0)
    return list

scale = int(input())
schedule = list(input().split(' '))
schedule = str_to_num(schedule)

location = [1, 1]

for var in range(len(schedule)):
    location[0] = location[0]+ schedule[var][0]
    location[1] = location[1]+ schedule[var][1]
    if location[0]<1:
        location[0] = location[0]+1
    if location[0]>scale:
        location[0] = location[0]-1
    if location[1]<1:
        location[1] = location[1]+1
    if location[1]>scale:
        location[1] = location[1]-1
    print('now location', location)
print(location)