while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a <= b:
        print("No")
    else:
        print("Yes")
[출처] [python] 백준 : 4101|작성자 코린이