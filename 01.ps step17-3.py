# 17-3 prefix sum
import sys
import string

input = sys.stdin.readline

s = input() # seungjaehwang
q = int(input()) # 4

char_list = {}
for char in string.ascii_lowercase:# a
        char_list[char] = [0] # {a : [0], b : [0]} 
        count = 0
        for i in range(len(s)): # 0 ~ 13
                if s[i] == char:
                        count += 1
                char_list[char].append(count)
        
for _ in range(q):
        char, start, end = input().rstrip().split()
        print(char_list[char][int(end) + 1] - char_list[char][int(start)])
