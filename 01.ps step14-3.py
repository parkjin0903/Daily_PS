# 14-3 

from math import factorial
num = int(input())

cnt = 0

for i in str(factorial(num))[::-1]:
  if i != '0':
    break
  cnt += 1

print(cnt)