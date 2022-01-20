# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    a_count = [0]
    c_count = [0]
    g_count = [0]
    t_count = [0]
    a = 0
    c = 0
    g = 0
    t = 0
    impacts = []

    for s in S:
        if s == 'A':
            a += 1
        elif s == 'C':
            c += 1
        elif s == 'G':
            g += 1
        elif s == 'T':
            t += 1
        a_count.append(a)
        c_count.append(c)
        g_count.append(g)
        t_count.append(t)
    print(a_count,c_count,g_count,t_count)
    
    for i in range(len(Q)):
        if a_count[Q[i]+1] - a_count[P[i]] > 0:
            impacts.append(1)
        elif c_count[Q[i]+1] - c_count[P[i]] > 0:
            impacts.append(2)
        elif g_count[Q[i]+1] - g_count[P[i]] > 0:
            impacts.append(3)
        elif t_count[Q[i]+1] - t_count[P[i]] > 0:
            impacts.append(4)
    return impacts
