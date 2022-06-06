N = int(input())
group = list(map(int, input().split()))
count = 0

for x in group: #1 3 5 7
    for i in range(2, x+1): #1 3 5 
        if x % i == 0:
            if x == i:
                count += 1
    
            break

print(count)