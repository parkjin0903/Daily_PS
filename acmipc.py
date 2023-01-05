def dfs(x, y):
    if graph[x][y] == '-':
        graph[x][y] = 1
        for _y in [1, -1]:
            Y = y + _y
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x, Y)

    elif graph[x][y] == '|':
        graph[x][y] = 1
        for _x in [1, -1]:
            X = x + _x
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X, y)

    else:
        return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = []
    cnt = 0
    for _ in range(n):
        graph.append(list(input()))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '-' or graph[i][j] == '|':
                dfs(i, j)
                cnt += 1
    
    print(cnt)

