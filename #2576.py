odd_li = []
for _ in range(7):
    n = int(input())
    if n%2:
        odd_li.append(n)
if odd_li:
    print(sum(odd_li))
    print(min(odd_li))
else:
    print(-1