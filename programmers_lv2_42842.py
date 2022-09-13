def solution(brown, yellow):
    num = brown - 4
    for i in range(1, num+1):
        if i * ((num-(2*i))//2) == yellow:
            break
    answer = [((num-(2*i))//2)+2 ,i+2]
    return answer