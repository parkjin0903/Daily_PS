n = int(input())
if n % 2 == 0:
    print("I LOVE CBNU")
elif n % 2 == 1:
    print("*"*n)
    print(" "*(n//2)+"*")
    for i in range(n//2):
        print(" "*(n//2 - i - 1)+"*"+" "*(1+i*2)+"*")