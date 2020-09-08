'''https://leetcode.com/problems/permutations/'''
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		rst = []
		def dfs(p):
			if p == len(nums):
				rst.append(nums[:])
			for i in range(p, len(nums)):
				nums[i], nums[p] = nums[p], nums[i]
				dfs(p+1)
				nums[i], nums[p] = nums[p], nums[i]
				
		dfs(0)
		return rst