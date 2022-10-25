# 11652

import sys
input = sys.stdin.readline

n = int(input())

card_dic = dict()

for _ in range(n):
    card = int(input())
    if card not in card_dic:
        card_dic[card] = 1
    else:
        card_dic[card] += 1



result = sorted(card_dic.items(), key = lambda item : (-item[1], item[0]))
print(result[0][0])