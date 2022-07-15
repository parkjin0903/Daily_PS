# 14-7 

from math import factorial

a, b = map(int, input().split())
print(factorial(a) // (factorial(b) * (factorial(a-b))))