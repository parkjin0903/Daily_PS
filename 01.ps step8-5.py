from math import sqrt

def Prime(num):
    if num == 1: 
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

base_list = list(range(2, 246912))

prime_list = []

for i in base_list:
    if Prime(i):
        prime_list.append(i)
        
while True:
    answer = 0
    n = int(input())
    if n == 0:
        break
    
    for j in prime_list:
        if n < j and j <= n*2:
            answer += 1
            
    print(answer)