#2667

num = int(input())
graph = []
house = []
cnt = 0
for i in range(num):
    array = list(map(int, input()))
    graph.append(array)

def dfs(x, y):
    global cnt
    if x < 0 or x >= num or y < 0 or y >= num:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # 검사 전에 다 1로 바꿔 버림
    
    return False # 1은 여기서 멈춤

result = 0
for i in range(num):
    for j in range(num):
        if dfs(i, j) == True:
            house.append(cnt)
            result += 1
            cnt = 0

house.sort()
        
print(result)
for i in range(len(house)):
    print(num[i])