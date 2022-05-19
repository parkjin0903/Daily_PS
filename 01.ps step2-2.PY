H, M = map(int, input().split())
time = int(input())
a = time // 60
b = time % 60
c= 0
if M + b >= 60:
    c = 1
    M = M + b - 60
    

elif M + b < 60:
    M = M + b
    
if H + a + c < 24:
    H = H + a + c
    
elif H + a + c >= 24:
    H = H + a + c - 24

print(H, M)
