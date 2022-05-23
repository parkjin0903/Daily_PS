num = int(input())
count = 0
list_sum = []
for _ in range(num):
    testcase = input()
    for i in range ((len(testcase))):
        if testcase[i] == 'O':
            count += 1
            list_sum.append(count)
        elif testcase[i] == 'X':
            count = 0
            list_sum.append(count)
    print(sum(list_sum))
    print(list_sum)
    
    