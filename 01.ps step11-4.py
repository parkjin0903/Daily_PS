import sys
from collections import Counter

num = int(input())
num_list = []

for _ in range(num):
  num_list.append(int(sys.stdin.readline()))

#1
print(round(sum(num_list)/num))
#2
num_list.sort()

print(num_list[int((num-1)/2)])
#3
cnt = Counter(num_list).most_common(2)

if len(num_list) > 1:
  if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
  else:
    print(cnt[0][0])
else:
  print(cnt[0][0])
#4
print(num_list[-1]-num_list[0])