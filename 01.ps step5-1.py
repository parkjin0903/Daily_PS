num1 = set(range(1,10001))
num2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num2.add(i)

num3 = sorted(num1 - num2)
for i in num3:
    print(i)
    