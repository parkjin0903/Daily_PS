def five_s_suffering(n):
    n_num_list = list(n)
    
    return sum([pow(int(num), 5) for num in n_num_list])

if __name__ == "__main__":
    n = input()
    
    print(five_s_suffering(n))