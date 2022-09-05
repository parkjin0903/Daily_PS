# 11479

word_list = input()
list1 = []
for i in range(len(word_list)):
    for j in range(i, len(word_list)): 
        list1.append(word_list[i:j+1])
print(len(set(list1)))
        