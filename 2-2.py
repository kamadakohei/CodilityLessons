# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()

    for i in range(len(A)):
        if i == len(A)-1:
            return A[i]
        
        if i % 2 == 0:
            if A[i] != A[i+1]:
                return A[i]
