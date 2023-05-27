import sys

input = sys.stdin.readline

n = int(input())

count = 0
list1 = []
for _ in range(n):
    temp = input().rstrip()
    if temp == "ENTER":
        set(list1)
        count += len(list1)
        list1 = []
        
    else:
        list1.append(temp)
        set(list1)
        list(list1)
    print(list1)

count += len(list1)

print(count)