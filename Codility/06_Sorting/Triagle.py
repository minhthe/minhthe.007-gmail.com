'''
https://app.codility.com/demo/results/training953UNF-5F3/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    A.sort()
    n = len(A)
    if n < 3: return 0
    for i in range(n-3, -1, -1  ):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0