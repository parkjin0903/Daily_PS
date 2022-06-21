import sys
input = sys.stdin.readline

n = int(input())

array_list = []
for i in range(n):
  [a, b] = map(int, input().split())
  array_list.append([a, b])

array_list.sort()

for list_index in range(n):
  print(array_list[i][0], array_list[i][1])