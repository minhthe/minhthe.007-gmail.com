'''
https://leetcode.com/problems/subsets/
'''
class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		tmp = [[]] 
		for i in range(len(nums)):
			n = []
			k = []
			for item in tmp:
				k = item + [nums[i]]
				n.append(k)
			tmp += n
		return tmp	