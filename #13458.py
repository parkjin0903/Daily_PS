# 13458

import math

class_num = int(input())
class_mates = list(map(int, input().split()))
class_mates.sort()
B, C = list(map(int, input().split()))
sum_list = list()
for class_index in class_mates:
    if class_index - B <= 0:
        sum_list.append(1)
        continue

    append_C = (class_index - B) / C
    math.ceil(append_C) 
    sum_list.append(math.ceil(append_C) + 1)

print(sum(sum_list))

# 오답 (난독)
''' 
class_num = int(input())
class_mates = list(map(int, input().split()))
class_mates.sort()
B, C = list(map(int, input().split()))
sum_list = list()
if B < C: 
    class_mates[0] = class_mates[0] - B
    for class_index in class_mates:
          append_C = class_index / C
          sum_list.append(math.ceil(append_C))

    if sum_list[0] <= 0:
        sum_list[0] = 1
    else:
        sum_list[0] += 1

else:
    class_mates[-1] = class_mates[-1] - B
    for class_index in class_mates:
          append_C = class_index / C
          sum_list.append(math.ceil(append_C))    

    if sum_list[-1] <= 0:
        sum_list[-1] = 1
    else:
        sum_list[-1] += 1

print(sum(sum_list))

print(sum_list)
'''