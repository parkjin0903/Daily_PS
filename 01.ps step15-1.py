
from itertools import permutations

n, m = map(int, input().split())

list1 = [i for i in range(1, n+1)]

per = list(permutations(list1, m))

for i in per:
  print(' '.join(map(str, i)))