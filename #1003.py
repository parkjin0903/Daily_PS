# 1003
import sys
input = sys.stdin.readline

T = int(input()) # 3
dp = [[1, 0], [0, 1]]
index_list = []
for i in range(T): 
    index_list.append(int(input())) # 0 1 3 
if max(index_list) >= 3:
    for j in range(2, max(index_list)+1): # 2
        a = dp[j-2][0] + dp[j-1][0]
        b = dp[j-2][1] + dp[j-1][1]
        dp.append([a,b])
for k in index_list:
    print(*dp[k])

    

