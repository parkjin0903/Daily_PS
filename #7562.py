import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs():
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y =  queue.popleft()
        if x == m and y == n:
            print(graph[x][y])
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<L and 0<=ny<L and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        

N = int(input())
for _ in range(N):
    L = int(input())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    
    graph = [[0] * L for _ in range(L)]
    bfs()
        