def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)
            
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)