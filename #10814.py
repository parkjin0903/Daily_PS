# 10814

N = int(input())

user_list = []

for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    user_list.append([age, name])

user_list.sort(key=lambda s: s[0])
for i in user_list:
    print(*i)