# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    stack = []
    record = 0
    for height in H:
        while(len(stack) != 0):
            pre_block = stack.pop()
            if pre_block == height:
                stack.append(pre_block)
                break
            elif pre_block < height:
                stack.append(pre_block)
                stack.append(height)
                break
            else:
                record += 1
        if len(stack) == 0:
            stack.append(height)
    
    return len(stack) + record
