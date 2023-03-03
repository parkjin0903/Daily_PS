from itertools import permutations as p

n, d = map(int, input().split())
for i in range(1, d):
    for j in p(list(set([i for i in range(d)])-set([i])), d-1):
        x = int(str(i)+''.join(map(str, j)), d)
        if x > n:
            print(x)
            exit()
print(-1)