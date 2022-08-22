# 1149

n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, len(dp)):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))


'''오답
N = int(input())

dp = [[[0]*3 for _ in range(3)] for _ in range(N)]

L = [[0]*3 for _ in range(N)]

for i in range(N):
    R, G, B = map(int, input().split())
    L[i][0], L[i][1], L[i][2] = R, G, B

for j in range(3):
    for k in range(3):
        dp[j][k][0] , dp[j][k][1], dp[j][k][2] = L[0][0], L[0][1], L[0][2]

for i in range(1, N):
    for j in range(3):
        R, G, B = map(int, input().split())
        dp[i][j][0] = dp[i-1]
'''