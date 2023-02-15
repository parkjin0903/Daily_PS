from math import factorial
N = int(input())
k = 0
while True:
    if N == 0:
        print('YES')
        break
    elif N < 0:
        print('NO')
        break
    N -= factorial(k)
    k += 1