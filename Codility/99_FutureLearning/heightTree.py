# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task

def solution(T):
    # write your code in Python 3.6
    pass
    if T  is None : return -1
    def f(T):
        stk = [(T, 0)]
        rst = -1
        while(len(stk)):
            u, l = stk.pop()
            rst = max(l,rst)
            if u.l :
                stk.append((u.l, l+1))
            if u.r:
                stk.append((u.r, l+1))
        return rst
    ans = f(T)
    return ans