'''
https://app.codility.com/demo/results/trainingXT7PQA-9GD/
'''
def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    t = (n+1)*(n+2) // 2
    return t - sum(A)
