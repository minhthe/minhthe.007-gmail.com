'''https://leetcode.com/problems/permutations'''
class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		rst = [[]]
		for item in nums:
			tmp = []
			for element in rst:
				for i in range(len(element)+1):
					tmp.append( element[:i] + [item] + element[i:]  )
			rst = tmp
		return rst