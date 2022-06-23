import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_list.append(sys.stdin.readline().strip())
set_list = set(num_list)
num_list = list(set_list)
num_list.sort()
num_list.sort(key = len)

for i in num_list:
    print(i)