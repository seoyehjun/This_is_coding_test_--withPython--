from collections import deque

graph = [[], [2,3,8], [1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False]*9

def dfs(graph, i, visited):
    visited[i] = True
    print(i,'노드 탐색')
    for var in graph[i]:
        if visited[var] == False:
            dfs(graph,var, visited)

def bfs(graph, i, visited):
    queue = deque([i])
    visited[i] = True
    
    while queue:
        v = queue.popleft()

        for var in graph[v]:#해당 노드가 탐색된적 있어도 해당노드 연결정보 검사
            #탐색여부 검사후 큐에 붙이고 탐색한다 큐에 붙이면 해당노드의 연결정보 검사해준다
            if visited[var] == False:
                queue.append(var)#큐에 붙이는건 노드의 인덱스이다
                visited[var] = True
                print(v,'노드 탐색')
