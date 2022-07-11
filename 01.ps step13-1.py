import sys
input = sys.stdin.readline

arr = []
dp = []

stair = int(input())
for _ in range(stair):
    arr.append(int(input()))

dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1]))
dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
for i in range(3,stair):
    dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

print(dp.pop())