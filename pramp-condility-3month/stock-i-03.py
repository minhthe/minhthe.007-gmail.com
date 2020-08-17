'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		rst = 0
		if not prices: return rst
		min_v = prices[0]
		for item in prices:
			rst = max(rst, item - min_v )
			min_v = min(min_v, item)
			
		return rst