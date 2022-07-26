# 18-1

import sys
input = sys.stdin.readline

coin_list = []

N, K = map(int, input().split())
for _ in range(N):
    coin_list.append(int(input())) # [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

count = 0

for div_num in reversed(coin_list):
    count += K // div_num
    K = K % div_num
    if K == 0 : 
        break

print(count)









