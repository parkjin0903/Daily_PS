def solution(s):
    list1 = []
    for i in s:
        if i == '(':
            list1.append(i)
        elif i == ')':
            if list1:
                list1.pop()
            elif not list1:
                return False
    if list1:
        return False

    return True