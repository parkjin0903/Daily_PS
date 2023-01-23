import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node] + 1
            answer[n] = node
            dfs(n)

N = int(input())

graph = [[] for _ in range(N+1)]
check = [0] * (N+1)
answer = [0] * (N+1)
for i in range(1, N):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)
dfs(1)
for i in range(2, N+1):
    print(answer[i])

