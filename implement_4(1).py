#9:40

scale_y, scale_x = map(int,input().split(' '))
has_been =[[0]*scale_x for _ in range(scale_y)]
#direction = 북-> 0, 동-> 1, 남-> 2, 서-> 3
location_y, location_x, direction = map(int,input().split(' '))
has_been[location_y][location_x] = 1 
geo = []
for var1 in range(scale_y):
    geo.append(list(map(int,input().split(' '))))
dxy = [(-1,0),(0,1),(1,0),(0,-1)]#각 방향당 이동 경로 미리 만들어둔다. (북,동,남,서)
#이동경로는 direction 숫자인덱스랑 대칭되게 정렬해놓는다. 

def turn_left():
    global direction
    direction -= 1
    if direction <0:
        direction
        direction = 3#0은 북쪽 3은 서쪽
moving =0
count =0
while True:
    count +=1
    if count<4:
        #방향 전환(이동할 위치 설정)     
        turn_left()
        print(count)
        print('direction',direction)
        print('location_x:',location_x,'location_y:',location_y)
        to_x = location_x + dxy[direction][0]
        to_y = location_y + dxy[direction][1]
        print('has_been[to_x][to_y]',has_been[to_x][to_y])
        print('geo[to_x][to_y]',geo[to_x][to_y])
        _=input()
        #이동조건 점검과 실제 이동
        if has_been[to_x][to_y] == 0 and geo[to_x][to_y] ==0:
            location_x = to_x
            location_y = to_y
            has_been[to_x][to_y]=1#기록 남기기
            count=0
            moving +=1
    
    else:
        #뒤로갈수 있는 경우 -물이 아닌경우(방향은 그대로 둔다)
        if geo[location_x*-1][location_y*-1] == 0:
            location_x= location_x+dxy[direction][0]*-1
            location_y= location_y+dxy[direction][1]*-1
            has_been[location_x][location_y] =1#기록 남기기
            direction +=1
            moving +=1
            count =0
        else:
            break    

print(moving)
    
        








