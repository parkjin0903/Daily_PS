# 14-5 
from collections import Counter

a = int(input())

for test_case in range(a):
  species = []
  b = int(input())
  for cloth in range(b):
    a, b = input().split()
    species.append(b)
  result_species = Counter(species)
  answer = 1  
  for key in result_species:
    answer *= result_species[key] + 1
  print(answer -1) 





