# 1018
'''
a, b = map(int, input().split())
cnt1 = 0
cnt2 = 0

for i in range(a): # 8
    if i % 2 == 0: # 0 
        list1 = list(map(str, input()))
        for j in range(len(list1)): # 8
            if j % 2 == 0:
                if list1[j] != 'B':
                    cnt1 += 1
            else:
                if list1[j] != 'W':
                    cnt1 += 1
    else:
        list1 = list(map(str, input()))
        for j in range(len(list1)):
            if j % 2 == 0:
                if list1[j] != 'W':
                    cnt1 += 1
            else:
                if list1[j] != 'B':
                    cnt1 += 1
    print(cnt1)

cnt2 = (a * b) - cnt1
print(min(cnt1, cnt2))
'''
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))