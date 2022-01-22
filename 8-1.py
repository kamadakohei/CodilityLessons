# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict
def solution(A):
    # write your code in Python 3.6
    if len(A)==0:
        return -1

    cnt_dic = defaultdict(int)

    for i in range(len(A)):
        cnt_dic[A[i]] += 1
    if max(cnt_dic.values()) <= len(A)/2:
        return -1
    
    return A.index(max(cnt_dic, key=cnt_dic.get))
