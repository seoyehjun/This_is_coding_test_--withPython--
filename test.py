from collections import deque


def dfs(graph, v, visited):
    visited[v] = True#v번째 노드는 방문완료
    print(v,end=' ')
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph, i , visited) #재귀



def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        


    
visited =[False]*9
graph = [ [], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
