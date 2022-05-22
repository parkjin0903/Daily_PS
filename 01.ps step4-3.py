list1 = set()
for _ in range(10):
    i = int(input())
    list1.add(i % 42)
    
print(len(list1))