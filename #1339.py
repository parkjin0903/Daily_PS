N = int(input())

words_list = []

for _ in range(N):
  words_list.append(input())

alpha_dict = {}

for word in words_list: # [GCF, ACDEB]
  word_len = len(word)-1 # 3 - 1 = 2
  for char in word:
    if char in alpha_dict:
      alpha_dict[char] += pow(10, word_len)
    else:
      alpha_dict[char] = pow(10, word_len)
    word_len -= 1

alpha_dict = sorted(alpha_dict.values(), reverse = True)

answer = 0
iter = 9

for value in alpha_dict:
  answer += value * iter
  iter -= 1

print(answer)