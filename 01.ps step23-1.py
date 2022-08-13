# 23-1

import sys
import headq as hq

n = int(input())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)