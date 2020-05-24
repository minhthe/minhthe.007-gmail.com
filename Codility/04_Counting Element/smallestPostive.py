def solution(A):
    # write your code in Python 3.6
    pass
    hs = {key: True for key in A}
    for i in range(1, 100001):
        if i not in hs:
            return i
    return 100001