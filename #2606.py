# 2606

import sys
input = sys.stdin.readline

computer = int(input())
pair = int(input())

graph = [[] for _ in range(computer + 1)]
for _ in range(pair):
    n, e = map(int, input().split())
    graph[n].append(e)
    graph[e].append(n)

visited = [False] * (computer + 1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)   

dfs(graph, 1, visited)

print(visited.count(True) - 1)
