# 9095 

T = int(input()) # 3
L = [0]

for _ in range(T):
    L.append(int(input())) # [0, 4, 7, 10]
max_l = max(L)
dp = [0] * (max_l+1)
dp[1], dp[2], dp[3] = 1, 2, 4
if max_l >= 4:
    for i in range(4, max_l+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in L[1:]:
    print(dp[i])
    
'''
N = int(input())
arr=[1,2,4]
for i in range(4,11):
    arr.append(sum(arr[-3:]))
for _ in range(N):
    T = int(input())
    print(arr[T-1])
'''
    