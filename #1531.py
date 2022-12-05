import sys
input = sys.stdin.readline

n = int(input())
length_N = len(str(n))

cnt = 0

for i in range(length_N - 1):
    cnt += 9 * 10 ** i * (i + 1)

print(cnt + (n - 10** (length_N - 1) + 1 ) * length_N)