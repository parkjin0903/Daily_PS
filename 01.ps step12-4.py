import sys

n = sys.stdin.readline().strip()
card = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline().strip()
test = list(map(int, sys.stdin.readline().split()))

dict = {}

for i in card:  # {-10:2, 2:1, 3:2, 6:1, 7:1, 10:3}
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in test:
    if i in dict:
        print(dict[i], end=" ")
    else:
        print(0, end=" ")
