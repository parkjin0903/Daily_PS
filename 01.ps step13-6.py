#not yet

import sys

input = sys.stdin.readline

k = int(input())

height = []
width = []
total = []

for i in range(6):
  direction, length = map(int, input().split())

  if direction == 1 or direction == 2:
    total.append(length)
    width.append(length)

  else:
    total.append(length)
    height.append(length)

big = max(height) * max(width)

max_heigth = total.index(max(height))
max_width = total.index(max(width))

small_height = abs(total[max_heigth-1]) - total[(max_heigth -5 if max_heigth == 5 else max_heigth + 1)]
small_width = abs(total[max_width-1]) - total[(max_width -5 if max_width == 5 else max_width + 1)]

answer = big - (small_height * small_width)
print(answer * k)
