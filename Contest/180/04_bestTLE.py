'''
https://leetcode.com/problems/maximum-performance-of-a-team/
'''
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        # print('hello')
        i = 0
        s = speed
        e = efficiency
        memo = {}
        rst = (0, int(1e9), 0)
        def f(i, k, s, e, memo, rst):
            # if((i, k) in memo): return memo[(i,k)]
            if(k == 0): return rst[2] 
            if(i == len(s)): return rst[2]
            
            x1,x2,x3 = rst[0],  rst[1], rst[2]
            rst2 = (  x1 + s[i] , min(x2, e[i])  , min(x2, e[i]) * (x1 + s[i] ) )
            pick = f(i+1, k-1, s, e, memo, rst2 )
            not_pick = f(i+1, k, s, e, memo, rst)
            memo[(i,k)] = max(pick, not_pick)
            return max(pick, not_pick)
            
            
            
        return f(i, k, s, e, memo, rst)