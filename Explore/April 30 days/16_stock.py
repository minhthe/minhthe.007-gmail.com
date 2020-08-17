'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/'''
class Solution(object):
	def maxProfit(self, prices):
		rst = 0 
		n = len(prices)
		if n == 0 : return 0
		left, right = [0] *(n), [0] * (n)
		min_v, ans = prices[0], 0
		
		for i in range(n):
			ans = max(ans, prices[i] - min_v)
			min_v = min(min_v, prices[i])
			left[i] = ans
		
		# 2 4 6 8 3 1 4 
		max_v, ans = prices[n-1], 0
		for i in range(n-1, -1, -1):
			ans = max(ans, (-prices[i] + max_v))
			max_v = max(max_v, prices[i])
			right[i] = ans

		for i in range(n):
			rst = max(rst, left[i] + right[i]) 
					
		return rst