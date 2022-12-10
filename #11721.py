import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dict_site = {}
for i in range(N):
    site, pw = input().split()
    dict_site[site] = pw

for i in range(M):
    site_temp = input().rstrip()
    print(dict_site[site_temp])