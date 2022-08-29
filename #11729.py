# 11729

n = int(input())

def towel(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        towel(n-1, a, c, b)
        print(a, c)
        towel(n-1, b, a, c)
print(2**n -1)

towel(n, 1, 2, 3)