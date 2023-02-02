import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(y, x):
    visited[y][x] = 1
    graph[y][x] = 0
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < w) and (0 <= ny < h):
            if visited[ny][nx] == 0:
                if graph[ny][nx] == 1:
                    dfs(ny, nx)

while True:
    w, h = map(int, input().split()) # 3 2
    cnt = 0
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)




