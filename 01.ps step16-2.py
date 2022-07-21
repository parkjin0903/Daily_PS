# 16-2
N = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746 # 나머지는 변하지 않으므로
print(dp[N])