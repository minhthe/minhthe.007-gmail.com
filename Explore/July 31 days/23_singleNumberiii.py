'''
https://leetcode.com/problems/single-number-iii
'''
import collections
class Solution:
	def singleNumber(self, nums: List[int]) -> List[int]:
		rst = []
		mp = collections.Counter(nums)
		for u,v in mp.items():
			if v == 1: rst.append(u)
		
		return rst