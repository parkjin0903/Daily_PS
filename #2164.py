# 2164

from collections import deque

queue = deque()

n = int(input())
for i in range(1, n+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    a = queue[0]
    queue.popleft()
    queue.append(a)

print(*queue)
