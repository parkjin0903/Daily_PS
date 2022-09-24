import sys
from collections import deque

input = sys.stdin.readline

graph = [0] * 100001

def bfs(N):
    queue = deque([N])
    while queue:
        a = queue.popleft()
        if a == K:
            print(graph[a])
            break
        for nx in [a-1, a+1, a*2]:
            if 0<= nx <= 100000 and not graph[nx]:
                graph[nx] = graph[a] + 1
                queue.append(nx)
                
N, K = map(int, input().split())

bfs(N)
                
        
    
    