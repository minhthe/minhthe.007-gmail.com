'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        rst = 0 
        min_v = prices[0]
        for i,v in enumerate(prices):
            min_v = min(min_v, v)
            rst = max(rst, v - min_v)
        
        return rst