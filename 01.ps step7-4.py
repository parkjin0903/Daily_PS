testset = int(input())
number = 0
for _ in range(testset):
    H, W, N = map(int, input().split())
    if N % H == 0:
    number = N // H
    floor = H
    else:  
    number = N // H + 1
    floor = N % H
    print(f'{floor*100+number}')

