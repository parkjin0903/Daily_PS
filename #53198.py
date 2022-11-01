from itertools import combinations

def solution(m, weights):
    answer = 0
    for i in range(len(weights)):
        com_list = list(combinations(weights, i + 1))
        for j in com_list:
            if m == sum(j):
                answer += 1
    return answer