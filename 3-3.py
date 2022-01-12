# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    entire_sum = sum(A)
    fir_sum = 0
    sum_list = []

    for i in range(len(A)-1):
        fir_sum += A[i]
        sum_list.append(abs(fir_sum-(entire_sum-fir_sum)))
    
    return min(sum_list)
