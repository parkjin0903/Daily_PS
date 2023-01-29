N = int(input())
for i in range(1, N+1):
    class_list = list(map(int, input().split()))
    del class_list[0]
    class_list.sort()
    max_num = 0
    for j in range(len(class_list)-1):
        temp_num = class_list[j+1] - class_list[j]
        if max_num < temp_num:
            max_num = temp_num
    
    print(f"Class {i}")
    print(f"Max {class_list[-1]}, Min {class_list[0]}, Largest gap {max_num}")
