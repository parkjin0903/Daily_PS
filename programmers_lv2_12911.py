def solution(n):
    bin_n = bin(n)[2:]
    
    while True:
        n += 1
        if str(bin_n).count('1') == str(bin(n)[:2]).count('1'):
            break
    
    return n
solution(78)