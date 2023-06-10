n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

check = []

def backtracking(start, depth):
    if depth == m:
        print(' '.join(map(str, check)))
        return
    for i in range(start, n):
        check.append(num_list[i])
        backtracking(i, depth + 1)
        check.pop()

if __name__ == "__main__":
    backtracking(0, 0)
