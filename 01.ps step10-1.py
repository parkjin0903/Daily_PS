N, M = map(int, input().split())
input_list = list(map(int, input().split()))

answer = 0

for i in range(len(input_list)-2):
  for j in range(i+1, len(input_list)-1):
    for k in range(j+1, len(input_list)):
      if input_list[i] + input_list[j] + input_list[k] > M:
        continue
      else: 
        answer = max(answer, input_list[i] + input_list[j] + input_list[k])

print(answer)