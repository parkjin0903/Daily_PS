from collections import Counter

species = []
a = int(input())
b = int(input())
for test_case in range(a):
  for cloth in range(b):
    a, b = map(int, input().split())
    species.append(b)
  result_species = Counter(species)  
  for key in result_species:
    answer *= result_species[key] + 1
  print(answer -1) 





