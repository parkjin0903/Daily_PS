# 1021 
1 2 3 4 5 6 7 8 9 10

from collections import deque

N, M = map(int, input().split())

dq = list(map(int, input().split()))
queue = deque(list(i for i in range(1, N+1)))

cnt = 0

for index in dq:
    