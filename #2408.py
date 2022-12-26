import sys

n = int(input())
cal = ''
for i in range(2*n-1):
    cal+=input()
cal = cal.replace('/', '//')
print(eval(cal))