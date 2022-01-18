# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(A, B, K):
    # write your code in Python 3.6
    def count_mod0(n,k):
        return math.floor((n+1)/k)

    return count_mod0(B,K) - count_mod0(A,K)
