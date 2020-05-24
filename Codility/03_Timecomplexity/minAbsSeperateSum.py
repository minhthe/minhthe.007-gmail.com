'''
https://app.codility.com/demo/results/trainingWMYBBC-GQM/

'''

def solution(A):
    # write your code in Python 3.6
    pass
    s = sum(A)
    m = 1e9   ### edge case with absoulte keyword
    t = 0
    for i in range(len(A)-1):
        t += A[i] 
        m = min(m , abs(s - 2*t))
    return m