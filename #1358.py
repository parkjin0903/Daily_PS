# 1358


W, H, X, Y, P = map(int, input().split())
cnt = 0

def people(x, y):
    global cnt

    if X <= x <= X+W:
        if Y <= y <= Y+H:
           cnt += 1

    elif x < X:
        if ((X - x)**2 + (Y + (H/2) - y)**2)**(0.5) <= (H/2):
            cnt +=1
    
    elif X+W < x:
        if ((X + W - x)**2 + (Y + (H/2) - y)**2)**(0.5) <= (H/2):
            cnt += 1
        
for _ in range(P):
    x, y = map(int, input().split())
    people(x, y)

print(cnt)
