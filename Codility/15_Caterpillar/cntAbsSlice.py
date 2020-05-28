'''
https://app.codility.com/demo/results/trainingXEPZJA-55U/

'''
def solution(A):

    n = len(A)
    if n == 1: return abs(A[0] * 2)
    A.sort()
    target = 0 
    left , right = 0 , n-1
    rst = int(1e14+1)
    while left < right:
        s = (A[left] + A[right])
        
        if s < target:
            left += 1 
        elif s > target:
            right -=1
        else:
            return target

        if  s < rst  :
            
            rst = min(rst, abs(s))
            
    tmp = min([abs(item * 2) for item in A])        
    return min(abs(rst), tmp)