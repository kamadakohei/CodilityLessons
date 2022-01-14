# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()

    for i in range(0,len(A)):
        if A[i] != i+1:
            return 0
            break
    return 1
