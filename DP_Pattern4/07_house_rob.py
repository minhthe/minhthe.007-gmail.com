'''https://leetcode.com/problems/house-robber/'''
class Solution:
	def rob(self, nums: List[int]) -> int:
		if len(nums) == 0: return 0
		current , pre = nums[0], 0 
		for item in nums[1:]:
			current, pre = max(pre + item, current ), current
		return current