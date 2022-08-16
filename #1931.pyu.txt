# 1931

N = int(input())
l = []
for _ in range(N):
    a, b = map(int, input().split())
    l.append([a, b])
l = sorted(l, key = lambda x: x[0])
l = sorted(l, key = lambda x: x[1])
last = 0
cnt = 0

for i, j in l:
    if i >= last:
        cnt += 1
        last = j
print(cnt)