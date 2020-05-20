'''
https://app.codility.com/demo/results/training6JMYX2-UMR/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    pass
    n = len(S)
    if n == 0: return -1
    if n == 1: return 0
    if n % 2 == 0: return -1
    pos = int((n-1)/2)
    # print(pos)
    k = 1
    while(pos + k < n):
        # print(S[pos+k])
        if(S[pos+k] != S[pos-k]):
            return -1
        k += 1
    return pos