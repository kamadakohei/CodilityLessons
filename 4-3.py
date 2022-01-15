def solution(N, A):
    List = [0]*N
    num = 0
    maxTF = False
    for i in A:
        if i <= N:
            List[i-1] += 1
            num = max(List[i-1],num)
            maxTF = False
        #カウンターが増加した時のみだけmaxを取る。
        elif maxTF == False:
             List = [num]*N
             maxTF = True
    return List
