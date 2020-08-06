'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		
		memo ={}
		def f(pos, l):
			if (pos,l) in memo: return memo[(pos, l)]
			if pos >= len(prices) or l >=2: return 0
			if l & 1: 
				pick = prices[pos] + f(pos+1, l+1) 
			else:
				pick = -prices[pos] + f(pos+1, l +1)
			not_pick = f(pos+1, l)
			memo[(pos,l)] = max(pick, not_pick)
			return memo[(pos, l)]
		return f(0,0)