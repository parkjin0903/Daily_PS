# 1654
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
l = []
for i in range(K):
    line = int(input())
    l.append(line)

start = 1
fin = max(l)



while start <= fin:
    line_number = 0
    mid = (start + fin) // 2 
    for i in l:
        line_number += i // mid
    if line_number >= N:
        start = mid + 1
    else:
        fin = mid - 1

print(fin)


