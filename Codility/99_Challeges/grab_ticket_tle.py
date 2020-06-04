'''
https://app.codility.com/demo/results/trainingNBQUE5-AU2/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    mp = {}
    tmp, arr, step= [], [] , 0
    def f(tmp,arr,step):
        cnt = 0 
        if len(tmp) == 3 and tuple(tmp) not in mp:
            mp[tuple(tmp)] = True
            return 1
        for i in range(step, len(A)):
            tmp.append(A[i])
            cnt += f(tmp,arr,i+1)
            tmp.pop()
        return cnt
    return f(tmp,arr,step)% int(1e9+7)