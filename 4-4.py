# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     positive_list = [i for i in A if i > 0]
#     unique_list = list(set(positive_list))
#     unique_list.sort()

#     if len(unique_list) == 0:
#         return 1
    
#     for i in range(1, len(unique_list)+1):
#         if i != unique_list[i-1]:
#             return i
#     return unique_list[-1]+1

# print(solution([1,-1,3,4,4,1,6,100000]))

def solution(A):
  ispositive = [False] * (10**7)

  for i in range(len(A)):
    if A[i] > 0:
      ispositive[A[i]] = True
  
  for j in range(1,len(ispositive)):
    if not ispositive[j]:
      return j


