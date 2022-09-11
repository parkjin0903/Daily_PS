from collections import deque

def solution(people, limit):
    
    queue = deque(sorted(people))
    cnt = 0
    while queue:
        if len(queue) >= 2:
            if queue[0] + queue[-1] > limit:
                queue.pop()
            else:
                queue.pop()
                queue.popleft()
            cnt += 1   
        else:
            queue.pop()
            cnt += 1
    
    return cnt