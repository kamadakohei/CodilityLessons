# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    min_value = 10**4
    min_index = 0
    for i in range(len(A)-1):
        if sum(A[i:i+2])/2 < min_value:
            min_value = sum(A[i:i+2])/2
            min_index = i
    
        if i < len(A)-2 and sum(A[i:i+3])/3 < min_value:
            min_value = sum(A[i:i+3])/3
            min_index = i
    return min_index
