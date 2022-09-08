def solution(s): # 01110
    count = 0
    count_0 = 0
    list_1 = []
    while str(s) != '1':
        
        for i in s:
            if i == '1':
                list_1.append(1) # 1 1 1
            elif i == '0':
                count_0 += 1 # 2
            
        b = int(bin(len(list_1))[2:])
        list_1 = []
        count += 1
        s = b
        s = str(s)
    return count,count_0