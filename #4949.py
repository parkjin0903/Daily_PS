# 4949

while True:
    a = input()
    stack = []
    if a == "." :
       break
    for text in a:
        if text == '[' or text =='(':
            stack.append(text)
        elif text == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else: 
                stack.append(']')
                break
        elif text == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

