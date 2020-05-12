'''
https://leetcode.com/problems/single-element-in-a-sorted-array/
'''
class Solution:
	def singleNonDuplicate(self, nums: List[int]) -> int:
		n = len(nums)
		if n==1: return nums[0]
		for i in range(0,len(nums)-2, 2):
			 if nums[i]!= nums[i+1]:
				 return nums[i]
		return nums[-1]