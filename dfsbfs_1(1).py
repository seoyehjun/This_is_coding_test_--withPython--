#11:15
from collections import deque



N, M = map(int,input().split(' '))

state = []

for var1 in range(N):
        state.append(list(map(int,input().split(' '))))


def dfs(y,x):
    if x <=-1 or x>=M or y<=-1 or y>=N:
        return False#이미 차 있음
    
    if state[y][x]==0:#dfs알고리즘에서 나타나는 절차 방문 확인-> 
        state[y][x] =1 #방문 표시
        dfs(y-1,x)#북
        dfs(y+1,x)#남
        dfs(y,x-1)#서
        dfs(y,x+1)#동
        return True#재귀 호출중에는 별 역할을 하지 않는 True
    return False#빈공간 아님

count =0
for var1 in range(N):#y값
    for var2 in range(M):#x값
        if dfs(var1,var2) == True:
            count +=1

print(count)


