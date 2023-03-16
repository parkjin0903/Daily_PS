import sys
from math import sqrt
si = sys.stdin.readline
 
c = -2*int(1e16)
mx = int((-1+sqrt(1-4*c))//2)+1
 
t = int(si())
while t:
    t -= 1
    n = int(si())
    s, e, ans = 0, mx, 0
    while s < e:
        mid = (s+e)//2
        if (mid+1)*mid//2 <= n:
            ans = mid
            s = mid+1
        else:
            e = mid
    print(ans)