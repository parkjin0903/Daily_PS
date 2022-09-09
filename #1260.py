# 1260

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, s, visited):
    visited[s] = True
    print(s, end=' ')
    graph[s].sort()
    for i in graph[s]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, s, visited):
    queue = deque([s]) # 1
    visited[s] = True    
    while queue:
        temp = queue.popleft()
        print(temp, end=' ')
        graph[temp].sort()
        for i in graph[temp]: # 2 3 4
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)
