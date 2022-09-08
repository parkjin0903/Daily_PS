def solution(s):
    list_int = list(map(int, s.split(' ')))    
    return str(min(list_int)) + ' ' + str(max(list_int))