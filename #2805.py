# 2805

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

start = 0
end = max(tree_list) # 20

while start <= end: 
    mid = (start + end) // 2 # 10
    spare = 0
    for i in tree_list:
        if i >= mid:
            spare += tree # 32
    if spare >= M:
        start = mid + 1 # start = 11 end = 20 mid = 15
    else:
        end = mid - 1
print(end)


'''
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan) #이분탐색 처음과 끝위치

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중
    for i in lan:
        lines += i // mid #분할 된 랜선 수
        
    if lines >= N: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)
'''
