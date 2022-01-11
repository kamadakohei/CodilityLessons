# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6

    n_bin = str(bin(N)[2:])
    n_bin = n_bin[n_bin.find('1'):n_bin.rfind('1')+1]
    n_bin_len = []
    n_bin = n_bin.split('1')

    for i in n_bin:
        n_bin_len.append(len(i))

    return max(n_bin_len)
