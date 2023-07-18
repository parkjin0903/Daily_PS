def sum3(n):
    n//=3
    return int (n*(2*3+(n-1)*3)/2)
def sum7(n):
    n//=7
    return int (n*(2*7+(n-1)*7)/2)
def sum21(n):
    n//=21
    return int (n*(2*21+(n-1)*21)/2)
n=int(input())
tmp=list(map(int,input().split()))
for i in tmp:
    print(sum3(i)+sum7(i)-sum21(i) )