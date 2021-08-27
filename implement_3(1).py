#5:31

def a_num(str):
    if str =='a':
        return 1
    if str =='b':
        return 2
    if str == 'c':
        return 3
    if str == 'd':
        return 4
    if str =='e':
        return 5
    if str == 'f':
        return 6
    if str == 'g':
        return 7
    if str == 'h':
        return 8

user_input = input()
user = [user_input[0],user_input[1]]
location = [int(a_num(user[0])),int(user[1])]


count = 0
if location[0]+2<9:
    if location[1]+1<9:
        count +=1
    if location[1]-1>0:
        count +=1
if location[0]-2>0:
    if location[1]+1<9:
        count +=1
    if location[0]-1>0:
        count +=1
if location[1]+2<9:
    if location[0]+1<9:
        count +=1
    if location[0]-1>0:
        count +=1
if location[1]-2>0:
    if location[0]+1<9:
        count +=1
    if location[0]-1>0:
        count +=1

print(count)