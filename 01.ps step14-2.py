#14-2

def GCD(num1, num2):
    while num2 != 0:
        a = num1 % num2
        num1 = num2
        num2 = a
    return num1


n = int(input())
list1 = list(map(int, input().split()))

for div_num in range(1, n):
    print(
        f"{list1[0]//GCD(list1[0], list1[div_num])}/{list1[div_num]//GCD(list1[0], list1[div_num])}"
    )