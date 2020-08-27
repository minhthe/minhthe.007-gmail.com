'''https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/'''
class Solution:
	def minOperations(self, nums: List[int]) -> int:
		s = 0 
		
		while(sum(nums) != 0):
			odd = False
			for i,v in enumerate(nums):
				if v & 1:
					odd = True
					s+=1
					nums[i] = v - 1
			if not odd 	:
				s+=1
				nums = [item//2 for item in nums]
		
		return s