def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    pos = -1
    rst = int(1e9)
    for i in range(n-1):
        t = A[i]
        for j in range(i+1,n):
            t += A[j]
            if rst > t / (j - i + 1):
                rst = t / (j - i + 1)
                pos = i
    return pos