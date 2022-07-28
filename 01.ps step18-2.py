# 18-2

n = int(input())
atm_list = list(map(int, input().split()))
atm_list.sort()
cumsum_list = [0 for _ in range(n)]
cumsum_list[0] = atm_list[0]
for i in range(1, n):
    cumsum_list[i] = cumsum_list[i-1] + atm_list[i]

print(sum(cumsum_list))

