'''
https://leetcode.com/problems/permutation-sequence/
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        arr = [i for i in range(1, n+1)]
        rst = []
        def f(arr,rst,l, r):
            if l == r:
                rst.append(arr[:])
            else:
                for i in range(l, r):
                    arr[i], arr[l] =arr[l], arr[i]
                    f(arr, rst, l+1, r)
                    arr[i], arr[l] =arr[l], arr[i]
            
            
        f(arr, rst,0, n)
        # print(rst)
        rst.sort()
        return ''.join(str(x) for x in rst[k-1])