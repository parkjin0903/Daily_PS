testcase = int(input())
for _ in range(testcase):
    num, word = input().split()
    for i in word:
        print(i*int(num),end='')
    print()