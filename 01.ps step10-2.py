num = input() # 216
answer = 0

for i in range(1, int(num)+1): # (216-27, 216)
  try_list = list(map(int, str(i)))
  result = i + sum(try_list)

  if result == int(num):
    print(i)
    break

  if i == int(num):
    print(0)
