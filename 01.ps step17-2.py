# 17-2 prefix sum

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
list1 = list(map(int, input().split()))
ans = [sum(list1[:K])] # 1
for i in range(N-K):
        ans.append(ans[-1]-list1[i]+list1[i+K])
print(max(ans))
