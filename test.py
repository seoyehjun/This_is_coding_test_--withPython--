from collections import deque


def dfs(graph, v, visited):#함수 1회 호출 == 탐색(visited - True로 설정)
    visited[v] = True#v번째 노드는 방문완료
    print(v,end=' ')
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph, i , visited) #재귀



def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node_linked = queue.popleft()
        for var in graph[node_linked]:
            if visited[var] == False:
                queue.append(var)
                visited[var] = True
                print('탐색',node_linked)



    
visited =[False]*9#인덱스 8까지 존재
graph = [ [], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
bfs(graph, 1, visited)
