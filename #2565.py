import sys
input = sys.stdin.readline

n = int(input()) # 8
dp = [1] * n # [1 2 2 1 1 1 1 1] [1 3 2 4 2 4 3 3]
list1 = sorted([list(map(int, input().split())) for _ in range(n)])
for i in range(n):
    for j in range(i):
        if list1[i][1] > list1[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))