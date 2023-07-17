a, b, c = map(int, input().split())
ls = [a*b*c, a*b, a*c, b*c, a, b, c]

max = ls[0]
for i in range(1,7):
    if(max%2 == 0 and ls[i]%2 == 0):  #둘 다 짝수
        if(max < ls[i]): max = ls[i]
    elif(max%2 == 0 and ls[i]%2 != 0):  #현재값이 홀수
        max = ls[i]
    elif(max%2 != 0 and ls[i]%2 == 0):  #현재 최댓값만 홀수
        max = max
    else:  #둘 다 홀수
        if(max < ls[i]): max = ls[i]

print(max)