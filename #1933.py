# 1932

n = int(input()) # 5

dp = []


for i in range(n):
    dp.append(list(map(int, input().split())))
# [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]
for j in range(1, len(dp)):
    dp[j][0] += dp[j-1][0]
    dp[j][-1] += dp[j-1][-1]
    for k in range(1, j):
        dp[j][k] += max(dp[j-1][k-1], dp[j-1][k])
        
print(max(dp[n-1]))