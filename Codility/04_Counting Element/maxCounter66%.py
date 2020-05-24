
'''
https://app.codility.com/demo/results/trainingA9S9BJ-CNB/
            
'''

def solution(N, A):
    # write your code in Python 3.6
    pass

    rst = [0] * N
    def increase(rst):
        m = max(rst)
        for i,v in enumerate(rst):
            rst[i] = m
        return rst
        
        
    for item in A:
        k = item - 1
        if item == N +1:
            rst = increase(rst)
        else:
            rst[k] += 1
    return rst