'''
https://app.codility.com/demo/results/trainingFCECUA-VEG/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    mp = {i: True for i in A}
    n = len(A)
    for i in range(1, n+2):
        if i not in mp:
            return i
    return 0