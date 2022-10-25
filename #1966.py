# 1966

from collections import deque

n = int(input())


for _ in range(n):
    M, N = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0
    while True:
        best = max(queue)
        front = queue.popleft()
        N -= 1
        if front == best:
            cnt += 1
            if N < 0:
                print(cnt)
                break

        else:
            queue.append(front)
            if N < 0 :
                N = len(queue) - 1