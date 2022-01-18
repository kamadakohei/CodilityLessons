# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    cnt = 0
    result = 0
    for i in range(len(A)):
        if A[i] == 0:
            cnt += 1
        else:
            result += cnt
        
        if result >= 10**9:
            return -1
    return result
        