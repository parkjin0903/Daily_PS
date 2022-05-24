testcase = int(input())
for _ in range(testcase):
    count = 0
    num = list(map(str, input().split()))
    student = sum(map(int,num[1:]))/int(num[0]) 
    for i in range(1, len(num)):
        if int(num[i]) > student:
            count += 1
    print("%.3f%%" %((count / int(num[0])*100)))
    
            
        
    
    
    
    
