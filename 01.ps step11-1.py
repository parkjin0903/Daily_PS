number = int(input())
answer_list = list()
for i in range(number):
  n = int(input())
  answer_list.append(n)

list(set(answer_list))
answer_list.sort()

for j in answer_list:
  print(j)