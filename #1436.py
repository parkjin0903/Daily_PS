from itertools import permutations

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    card = input()
    cards.append(card)

result = set()

for i in permutations(cards, k):
    print(i)
    result.add(''.join(i))

print(result)

print(len(result))