# 1269

a, b = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = set(list_a) ^ set(list_b)
print(len(list_c))