'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		rst = 0
		
		min_v = int(1e9)
		for i ,v in enumerate(prices):
			min_v = min(v, min_v)
			rst = max(rst, v - min_v)
			
		return rst