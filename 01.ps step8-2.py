M = int(input())
N = int(input())

answer = list()
for number in range(M, N+1):
    if number == 1:
        pass
    elif number == 2:
        answer.append(number)
    else:
        for divide_num in range(2, number):
            if number % divide_num == 0:
                break
            elif divide_num == number - 1:
                answer.append(number)

if len(answer) == 0:
    print('-1')
else:
    print(sum(answer))
    print(min(answer))        