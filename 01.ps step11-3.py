import sys

number = int(input())
index_list = [0] * 10001
answer_list = list()
for i in range(number):
    index_list[int(sys.stdin.readline())] += 1
for i in range(10001):
    if index_list[i] != 0:
        for j in range(index_list[i]):
            print(i)