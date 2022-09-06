# 25305

N, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = sorted(list1, reverse=True)
print(list2[k-1])

