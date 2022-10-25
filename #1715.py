# 1715

import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    temp = []
    for i in range(N):
        card = int(input())
        heapq.heappush(temp, card)

    if N == 1:
        print(0)
    else:
        answer = 0
        while len(temp) > 1:
            temp1 = heapq.heappop(temp)
            temp2 = heapq.heappop(temp)
            answer += temp1 + temp2
            heapq.heappush(temp, temp1 + temp2)
        print(answer)
if __name__ == '__main__':
    main()
    
            