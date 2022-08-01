# 19-1

import sys

def main():
   
    def push(x):
        stack.append(x)

    def pop():
        return -1 if not stack else stack.pop()
           
    def size():
        return len(stack)

    def empty():
        return 0 if stack else 1

    def top():
        return stack[-1] if stack else -1

    N = int(sys.stdin.readline().rstrip())
    stack = list()

    for _ in range(N):
        command = sys.stdin.readline().rstrip().split()

        if command[0] == "push":
            push(command[1])
        elif command[0] == "pop":
            print(pop())
        elif command[0] == "size":
            print(size())
        elif command[0] == "empty":
            print(empty())
        elif command[0] == "top":
            print(top()) 

if __name__ == "__main__":
    main()