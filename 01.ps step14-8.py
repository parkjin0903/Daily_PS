# 14-8

from math import factorial

a, b = map(int, input().split())
b = min(b, a-b)

for i in range(1, b):
  a *= a-i

for i in range(1, b+1):
  a //= i

print(a % 10007)