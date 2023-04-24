def propose(cnt):
    if cnt ==0:
        print("끝")
        break
    print("고백할게")
    propose(cnt-1)

propose(5)