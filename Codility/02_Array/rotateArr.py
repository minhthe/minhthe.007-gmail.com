def solution(A, K):
    # write your code in Python 3.6
    pass
    n = len(A)
    if n == 0 : return []
    K = K % n
    return   A[-K:] + A[:-K] 