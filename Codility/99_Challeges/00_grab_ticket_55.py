'''
https://app.codility.com/demo/results/trainingTEPQW5-PAP/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    rst = []
    mp = {}
    def f():
        cnt = 0
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n):
                    tmp = [A[i], A[j], A[k]]
                    if tuple(tmp) not in mp :
                        cnt +=1
                        mp[tuple(tmp)] = True
        return cnt
    return f()