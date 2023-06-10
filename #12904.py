word1 = list(input())
word2 = list(input())

while len(word1) != len(word2):
    if word2[-1] == 'A':
        word2.pop()

    elif word2[-1] == 'B':
        word2.pop()
        word2.reverse()


if word1 == word2:
    print('1')
    
else:
    print('0')
    