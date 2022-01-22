# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    stack = []
    c = 0

    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while(len(stack)!=0):
                if stack[-1] > A[i]:
                    c += 1
                    break
                elif stack[-1] < A[i]:
                    stack.pop()
                    c += 1
    return len(A) - c
