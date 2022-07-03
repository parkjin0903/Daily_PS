# 14-6

M, N = map(int, input().split())

def countnum(num1, num2):
  count = 0
  while num1 != 0 :
    num1 = num1 // num2
    count += num1
  return count 

print(min(countnum(M, 2) - countnum(M-N, 2) - countnum(N, 2)), countnum(M, 5)- countnum(M-N, 5) - countnum(N, 5)) 


