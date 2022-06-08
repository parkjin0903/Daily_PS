N = int(input()) 

if N == 1:
    print('')

for divide_num in range(2, N+1):
    if N % divide_num == 0:
        while N % divide_num == 0:
            print(divide_num)
            N = N / divide_num