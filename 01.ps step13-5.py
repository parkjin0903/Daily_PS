import sys
input = sys.stdin.readline

while True:

  list1  = list(map(int, input().split()))
  list1.sort()
  if list1[0] == 0 and list1[1] == 0 and list1[2] == 0 :
    break
  elif list1[0]**2 + list1[1]**2 == list1[2]**2:
    print('right')
  else:
    print('wrong')