# 14-9

from math import factorial

a, b = map(int, input().split())
b = min(b, a-b)

num = a
for i in range(1, b):
  a *= num-i


for i in range(1, b+1):
  a //= i

if b != 0:
    print(a % 10007)
elif b == 0:
    print(1)