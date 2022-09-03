# 9465

def dp():
    n = int(input())
    arr1 = list(map(int, input().split())) # 50 10 100 20 40
    arr2 = list(map(int, input().split())) # 30 50 70 10 60
    arr3 = []
    dp1 = [0] * (n+1)
    dp2 = [0] * (n+1)
    arr3.append(for pair in zip(arr1, arr2)) # [[50, 30], [10, 50], [100, 70], [20, 10], [40, 60]]
    db1 = arr3[0][0]
    db2 = arr3[0][1]
    for i in range(1, len(arr3)):

'''
t = int(input())
for i in range(t):
  s = []
  n = int(input())
  for k in range(2):
    s.append(list(map(int, input().split())))
  for j in range(1, n):
    if j == 1:
      s[0][j] += s[1][j - 1]
      s[1][j] += s[0][j - 1]
    else:
      s[0][j] += max(s[1][j - 1], s[1][j - 2])
      s[1][j] += max(s[0][j - 1], s[0][j - 2])
  print(max(s[0][n - 1], s[1][n - 1]))
'''         


    '''

T = int(input())
for _ in range(T):
    n = int(input())
    for _ in range(2):
        array

        1 1 2 3 5 8 13

    dp = []
    dp[i] = dp[i-1] + dp[i-2]
'''