def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    mp = {i+1: 1 for i in range(n) }
    hs = {}
    for item in A:
        hs[item] = 1 if item not in hs else hs[item]  + 1
    for key in hs:
        if key not in mp:
            return 0
        if hs[key] != 1:
            return 0
    return 1