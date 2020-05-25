'''
https://app.codility.com/demo/results/trainingW5GEUE-EQB/
'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    if n == 1 : return 0
    
    def f(arr):
        rst = []
        
        cnt = {}
        max_v = arr[0]
        for i in range(0, len(arr)):
            cnt[arr[i]] = 1 if arr[i] not in cnt else cnt[arr[i]]+1
            
            if cnt[arr[i]] >= cnt[max_v]:
                max_v = arr[i]
            
            if cnt[max_v] > ( i+1 ) // 2:
                rst.append(max_v)
            else:
                rst.append('e')
        return rst
            
            
        
        
    a= f(A)
    b= f(A[::-1])
    b= b[::-1]
    # print(a)
    # print(b)
    def compare(a,b):
        cnt = 0 
        for i in range(len(a)-1):
            if a[i] == b[i+1] and a[i]!='e':
                cnt+=1
        return cnt
    ans = compare(a,b)
    return ans