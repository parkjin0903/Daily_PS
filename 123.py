#  11660

n, m = map(int, input().split()) # 4 3
l2 = [[0, 0, 0, 0, 0]]
ans = 0
for _ in range(n): # 4
    l1 = []
    l1.append(0) # [0]
    l0 = list(map(int, input().split())) # [1, 2, 3, 4]
    l1 = l1 + l0 # [0, 1, 2, 3, 4]
    for i in range(1, len(l1)):        
        l1[i] += l1[i-1] # [0, 1, 3, 6, 10]
    l2.append(l1) # [[0, 1, 3, 6, 10], [0, 2, 5, 9, 14], [0, 3, 7, 12, 18]...]

for i in range(m):
    x1, x2, y1, y2 = map(int, input().split()) # 2 2 3 4
    if x1 == y1:
        ans = l2[x1][y2] - l2[x1][x2-1]
    elif x1 != y1:
        for j in range(x1, y1+1): # (2, 4)
            ans += l2[j][y2] - l2[j][x2-1] # l2[2][4] = l2[2][1]
    print(ans)
    ans = 0
