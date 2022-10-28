import sys
import heapq
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    word = int(input())
    list_temp = list(map(int, input().split()))
    heapq.heapify(list_temp)
    answer = 0
    while len(list_temp) > 1:
        temp1 = heapq.heappop(list_temp)
        temp2 = heapq.heappop(list_temp)
        answer += temp1 + temp2
        heapq.heappush(list_temp, temp1 + temp2)
        print(answer)
    print(answer)
