a = int(input())
list1 = list(map(int, input().split()))

b = max(list1)
aver_list = [list1[i]/b*100 for i in range(a)]
print((sum(aver_list))/a)