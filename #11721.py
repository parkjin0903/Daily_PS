ex_str = input()
ans_str = ''
for i in range(1, len(ex_str)+1):
    ans_str += ex_str[i-1]
    if i % 10 == 0:
        print(ans_str)
        ans_str = ''
if ans_str:
    print(ans_str)