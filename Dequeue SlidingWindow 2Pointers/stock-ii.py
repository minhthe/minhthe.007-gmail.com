'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        rst = 0 
        
        start = 0 
        
        for end in range(1, len(prices)):
            if(prices[end] > prices[start]):
                rst+= prices[end] - prices[start]
            start = end

                
        
        return rst