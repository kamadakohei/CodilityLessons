# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    distinct_valueset = set()
    for a in A:
        distinct_valueset.add(a)

    return len(distinct_valueset)
         