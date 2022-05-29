dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num = input()
count = 0
for j in range(len(num)):
    for i in dial:  
        if num[j] in i:
            count += dial.index(i)+3
print(count)
