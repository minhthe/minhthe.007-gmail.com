'''https://leetcode.com/problems/maximum-subarray'''
class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_end = nums[0]
		s = 0 
		for i, v in enumerate(nums):
			s += v
			if s > max_end:
				max_end = s
			if s <= 0 :
				s = 0 
		return max_end