from sympy import N


N = int(input())
new_N = N
cnt = 0

while True:
    new_N = (new_N % 10) * 10 + (new_N // 10 + new_N % 10) % 10
    cnt += 1
    if new_N == N :
            break
        
print(cnt)       