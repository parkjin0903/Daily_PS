N = int(input())

for i in range(N):
    print(' '* i, end= '')
    print('*'*((2*(N-i))-1))
for j in range(1, N):
    print(' '* (N-j-1), end = '')
    print('*'* (j*2+1))