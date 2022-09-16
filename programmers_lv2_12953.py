def solution(arr):
    multiple = 1
    for i in arr:
        multiple *= i
    
    for i in range(max(arr), multiple+1):
        cnt = 0
        for j in arr:
            if i % j == 0:
                cnt +=1
        if cnt == len(arr):
            return i            
  

