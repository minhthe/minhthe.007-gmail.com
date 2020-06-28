'''
https://leetcode.com/problems/the-kth-factor-of-n/
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        def f(n):
            rst = []
            for i in range(1, int( n**(0.5)) + 1):
                if n % i == 0:
                    rst.append(i)
                    if n//i != i : rst.append(n//i)
            return rst
            
        arr = f(n)
        arr.sort()
        if len(arr) < k : return -1
        else: return arr[k-1]
        