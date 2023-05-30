n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

check = []

def backtracking(depth):
    if depth == m:
        print(*check)
        return

    for i in range(n):
        if num_list[i] in check:
            continue
        check.append(num_list[i])
        backtracking(depth + 1)
        check.pop()


if __name__ == "__main__":
    backtracking(0)