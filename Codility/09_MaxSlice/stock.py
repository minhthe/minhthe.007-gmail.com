# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6
#     pass
#     rst = 0 
#     n = len(A)
#     if n <  2 : return 0
    
#     for i in range(n-1):
#         for j in range(i+1, n):
#             rst = max(rst, -A[i] + A[j])
#     return rst
def solution(A):
    
    n = len(A)
    if n < 2: return 0
    min_v, max_v = A[0] ,0 
    rst = 0
    for i in range(1, n):
        if A[i] > min_v:
            max_v = A[i]
            rst = max(max_v - min_v, rst)
        if min_v > A[i]:
            min_v = A[i]
        
    return rst
        