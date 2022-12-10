import sys

input = sys.stdin.readline

N, M = map(int, input().split())

list_ans = []

for i in range(N):
    list_temp = list(map(int, input().split()))
    for i in range(len(list_temp)-1):
        list_temp[i+1] += list_temp[i]
    list_ans.append(list_temp)

num = int(input())

# 1 3 7
# 8 24 56

print(list_ans)

for _ in range(num):
    i, j, x, y = map(int, input().split()) # 1 2 1 2
    ans = 0
    for k in range(i - 1, x):
        if j == 1:
            ans += list_ans[k][y-1]
        else:
            ans += list_ans[k][y-1] - list_ans[k][j-2]
    print(ans)
    

        