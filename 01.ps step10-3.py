rot_num = int(input())
group_list = []
answer_list = []

for _ in range(rot_num):
  weight, height = map(int, input().split())
  group_list.append((weight, height))

for i in range(rot_num):
  count = 1
  for j in range(rot_num):
    if group_list[i][0] < group_list[j][0] and group_list[i][1] < group_list[j][1]:
      count += 1
  answer_list.append(count)

print(*answer_list)

