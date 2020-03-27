'''
https://leetcode.com/problems/pizza-with-3n-slices


more explanation:
https://leetcode.com/problems/pizza-with-3n-slices/discuss/548711/Java-Solution-Memo

https://leetcode.com/problems/pizza-with-3n-slices/discuss/551604/From-O(n!)-to-O(2n)-to-O(n)
'''
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        t = int(len(slices)/3)
        print(t)
        memo = {}
        def f(a, p, cnt, t, memo):
            if( (p,cnt) in memo ): return memo[(p,cnt)]
            
            if(t == cnt or p >= len(a)): 
                memo[(p,cnt)] = 0
                return 0
            
            pick = a[p] + f(a, p + 2, cnt +1 ,t, memo)
            skip = f(a, p+1, cnt, t  , memo)
            memo[(p,cnt)] = max(pick, skip)
            return memo[(p,cnt)]
                   
            
        a= f(slices[:len(slices) - 1], 0, 0, t,memo)
        memo = {}
        
        
        b = f(slices[1:], 0, 0, t, memo)
        
        return max(a,b)