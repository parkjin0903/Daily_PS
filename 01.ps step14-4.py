#14-4
from math import factorial
num = int(input())

for _ in range(num):
  a, b = map(int, input().split())
  print(factorial(b) // (factorial(a) * (factorial(b-a))))