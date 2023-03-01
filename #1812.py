n = int(input())
s = []
sum = 0
for i in range(n):
    a = int(input())
    s.append(a)
    sum += a
sum //= 2
for i in range(n):
    num = 0
    for j in range(1, n, 2):
        num += s[(i + j) % n]
    print(sum - num)