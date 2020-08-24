'''https://leetcode.com/problems/maximum-number-of-coins-you-can-get'''
class Solution:
	def maxCoins(self, piles: List[int]) -> int:
		rst = 0 
		piles.sort()
		for i in range( len(piles)//3,len(piles), 2  ):
			rst += piles[i]
		return rst