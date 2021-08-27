#9:40

scale_y, scale_x = map(int,input().split(' '))
has_been =[[0]*scale_x for var in range(scale_y)]
#direction = 북-> 0, 동-> 1, 남-> 2, 서-> 3
location_y, location_x, direction = input().split(' ')
has_been[location_y][location_x] = 1 
geo = []
for var1 in range(scale_y):
    geo.append(list(map(int,input().split(' '))))
dxy = [(-1,0),(0,1),(1,0),(0,-1)]#각 방향당 이동 경로 미리 만들어둔다. (북,동,남,서)
#이동경로는 direction 숫자인덱스랑 대칭되게 정렬해놓는다. 

def turn_left():
    if direction>=0:
        global direction 
        direction -= 1
    else:
        global direction
        direction =3

while True:
    turn_left()
    to_x = location_x + dxy[direction][0]
    to_y = location_y + dxy[direction][1]

    if has_been[to_x][to_y] == 0 and geo ==0:
        location_x = to_x
        location_y = to_y
        








