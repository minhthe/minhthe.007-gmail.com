'''
https://app.codility.com/demo/results/training3RSP3G-BRW/

'''
def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    m = max(A)
    if m!=n :return 0
    mp = {}
    for item in A:
        if item in mp:
            return 0
        else:
            mp[item] = True
    return 1