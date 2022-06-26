import sys


card_num = int(input())
card = list(map(int, sys.stdin.readline().split()))
check_num = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(check_num):
    if binary_search(card, check[i], 0, card_num - 1) is not None:
        print(1, end=" ")
    else:
        print(0, end=" ")
