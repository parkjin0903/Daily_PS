def find(num):
    for i in range(2, int(int(num)**0.5)+1):
        if int(num) % i == 0:
            return
            
    if len(num) == n:
        print(num)
        return

    for p in prime:
        find(num+p)
    
n = int(input())
start = ['2', '3', '5', '7']
prime = ['1', '3', '7', '9']
for s in start:
    find(s)