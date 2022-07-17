# 17-1 prefix sum
input = sys.stdin.readline
n, m = map(int, input().split()) # 5 3

pfs = list(map(int, input().split())) # 5 4 3 2 1 

for i in range(n-1): 
    pfs[i+1] += pfs[i] # 5 9 12 14 15
pfs = [0] + pfs # 0 5 9 12 14 15

for _ in range(m):
    a, b = map(int, input().split())
    print(pfs[b]-pfs[a-1])