# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []

    for s in S:
        if s == ')':
            if len(stack) == 0:
                return 0
            c = stack.pop()
            if c == '(':
                continue
            else:
                return 0
        
        elif s == ']':
            if len(stack) == 0:
                return 0
            c = stack.pop()
            if c == '[':
                continue
            else:
                return 0
        
        elif s == '}':
            if len(stack) == 0:
                return 0
            c = stack.pop()
            if c == '{':
                continue
            else:
                return 0
        
        else:
            stack.append(s)
    if len(stack) == 0:
        return 1
    else:
        return 0
