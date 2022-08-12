# 22-1

n = int(input())
l1 = list(map(int, input().split()))
l1.sort() # 1 2 3 4 5
m = int(input())
l2 = list(map(int, input().split()))
l2.sort() # 1 3 7 9 5
def bin_search(list1, list2):
    for i in range(len(list2)): 
        if list2[i] == list1[n//2]:
            print(1)
        elif list2[i] >= list1[n//2]:
            
