import sys

num = int(input())

for i in range(num+1):
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)