import sys
input = sys.stdin.readline

def main():
    N = int(input())
    temp = []
    ans = 0
    for i in range(N):
        card = int(input())
        temp.append(card)

    temp.sort()

    if N == 1:
        return card
    
    elif N == 1:
        return sum(temp)
    
    else:
        cnt = N-2
        ans += (temp[0] + temp[1]) * (N-1)
        while cnt > 0:
            for i in range(2, len(temp)-2):
                ans += temp[i] * cnt
                cnt -= 1
        return ans

if __name__ == '__main__':
    main()
    
            