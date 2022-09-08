def solution(s):
    list1 = s.split(' ')
    list2 = []
    for text in list1:
        list2.append(text.capitalize())
    return ' '.join(list2)