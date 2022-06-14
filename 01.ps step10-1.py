num = input() # 216
len_num = len(num) * 9 # 27
answer = 0

for i in range(int(num)-len_num, int(num)): # (216-27, 216)
  for j in range(len(str(i))): #3 
    answer += int(str(i)[j])  

  if answer + i != int(num):
    continue 
    
  else:
    print(i)