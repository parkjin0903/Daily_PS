def solution(n):
    dp = [0] * 100001
    dp[1], dp[2] = 1, 1
    if n >= 3:
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
    return dp[n] % 1234567