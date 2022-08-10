# 18-4
def main():

    mathexp_list = input().split('-') # ['55+30', '50+40']
    result = sum(map(int, (mathexp_list[0].split('+'))))
    for index_num in range(1, len(mathexp_list)):
        result -= sum(map(int, (mathexp_list[index_num].split('+'))))
    print(result)


if __name__ == '__main__':
   main()