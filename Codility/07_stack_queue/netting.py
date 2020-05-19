# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    pass
    stk = []
    for item in S:
        if len(stk):
            if(item == ")" and stk[-1] == "("):
                stk.pop()
                continue
        stk.append(item)
    return 1 if len(stk) == 0 else 0