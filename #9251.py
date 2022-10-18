import sys
input = sys.stdin.readline

word1 = input()
word2 = input()

temp = [0] * len(word2)

for i in range(len(word1)):
    cnt = 0
    for j in range(len(word2)):
        if cnt < temp[j]:
            cnt = temp[j]
        elif word1[i] == word2[j]:
            temp[j] = cnt + 1

print(max(temp)-1)
