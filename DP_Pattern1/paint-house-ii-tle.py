'''
https://www.lintcode.com/problem/paint-house-ii/
lte -> 85 %
'''
class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        n = len(costs)
        if n == 0 : return 0
        
        k = len(costs[0])
        if k == 0: return 0
        # if n == 1: return min(costs[0])
        ans = int(1e9)
        memo = {}
        def f(r,h):
            if (r,h) in memo: return memo[(r,h)]
            
            if r >= n: return 0
            
            rst = int(1e9)
            for i in range(k):
                if i==h:
                    continue
                rst = min(rst, costs[r][i] + f(r+1, i))    
                
            memo[(r,h)] =  rst
            return rst
            
        for i in range(k):
            ans = min(ans , costs[0][i] + f(1, i))
        return ans