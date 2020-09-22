'''https://leetcode.com/problems/majority-element'''
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		
		candidate = None
		cnt = 0 
		for item in nums:
			if cnt == 0: 
				candidate = item
			# else:
			cnt = cnt + 1 if item == candidate else cnt - 1
		return candidate