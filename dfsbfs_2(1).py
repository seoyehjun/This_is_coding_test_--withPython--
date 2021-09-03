#4: 41
from collections import deque

N,M = map(int,input().split(' '))
geo = []

#맵 입력받기(띄어쓰기 없다)
for var in range(N):
    geo.append(list(map(int,input())))

direc = [(-1,0),(1,0),(0,-1),(0,1)]

def route(y,x):
    que = deque()
    que.append((y,x))
    count =0
    while que:
        print('count',count)
        print('que',bool(que))
        y, x = que.popleft()
        
        for i in range(4):
            ny = y+direc[i][0]
            nx = x+direc[i][1] 
            print('ny',ny)
            print('nx',nx)
            #큐에 넣을 수 없는 배재사례2건
            #1.범위밖 인덱스
            #2.괴물이 있는 위치
            if ny<0 or ny>=N or nx<0 or nx>=M:
                continue
            print(geo[ny][nx])
            if geo[ny][nx] == 0:
                continue
            #큐에 넣는 절차 시작
            if geo[ny][nx] == 1:
                que.append((ny, nx))#지정 위치에서 다시 4방향 검사 
                geo[ny][nx] = geo[y][x] + 1#해당위치까지의 거리 
    
    return geo[N-1][M-1]


print(route(0,0))
print(geo)

        

