# 18870

import sys
input = sys.stdin.readline

N = int(input())
list1 = list(map(int, input().split())) # 2 4 -10 4 -9
list2 = list(set(list1))
list2.sort() # -10 -9 2 4 4

dic = {list2[i] : i for i in range(len(list2))}
for i in list1:
    print(dic[i], end =' ')