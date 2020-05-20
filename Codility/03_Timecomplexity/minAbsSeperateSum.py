# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    s = sum(A)
    m = 1e9   ### edge case
    t = 0
    for i in range(len(A)-1):
        t += A[i] 
        m = min(m , abs(s - 2*t))
    return m