M, N = map(int, input().split())
for number in range(M, N+1):  
  if number == 1:
    continue #pass continue
  
  for divide_num in range(2, int(number ** 0.5)+1):
    if number % divide_num == 0:
      break
      
  else:
    print(number)
  