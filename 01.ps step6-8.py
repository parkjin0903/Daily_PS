cnt = int(input())

for i in range(cnt):
    word = input()
    
    for j in range(len(word)):
        
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1    
            break
    
print(cnt)
