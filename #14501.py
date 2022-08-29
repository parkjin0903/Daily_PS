# 14501

N = int(input())
dp = []

for _ in range(N):
    arr = list(map(int, input().split()))
    dp.append([arr for _ in range(N)])

for i in range(N):
    

print(dp)