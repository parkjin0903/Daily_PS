import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1
    current_color = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < N) and (0 <= ny < N):
            if visited[nx][ny] == 0:
                if graph[nx][ny] == current_color:
                    dfs(nx, ny)
                    if graph[x][y] == 'R':
                        graph[x][y] = 'G'

N = int(input())

graph = [list(input()) for _ in range(N)]
visited = [[0] * (N) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rgb_cnt = 0
gb_cnt = 0

for i in range(N):
    for j in range(N):
        if visited == 0:
            dfs(i, j)
            rgb_cnt += 1

visited = [[0] * (N) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            gb_cnt += 1

print(rgb_cnt, gb_cnt)        


