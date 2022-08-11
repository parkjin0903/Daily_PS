# 19-2 
import sys
input = sys.stdin.readline

money_list = []

num = int(input())

for _ in range(num):
    input_num = int(input())
    if input_num != 0:
        money_list.append(input_num)
    elif input_num == 0:
        money_list.pop()

print(sum(money_list))                                 