import sys

number = int(input())
answer_list = list()
for i in range(number):
  answer_list.append(int(sys.stdin.readline()))

list(set(answer_list))
answer_list.sort()

for j in answer_list:
  print(j)