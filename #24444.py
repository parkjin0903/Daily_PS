# 24444

from collections import deque
# input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 1


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    global count    
    queue = deque([start]) # 1
    visited[start] = count

    while queue:
        v = queue.popleft()
        graph[v].sort() # [2, 4]
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                count += 1
                visited[i] = count

bfs(graph, 1, visited)

for i in range(1, N+1):
    print(visited[i])
