'''
https://leetcode.com/problems/subsets-ii/
'''
class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		rst = []
		tmp = []
		step = 0
		mp = {}
		def f(rst, tmp, step):
			if tuple(sorted(tmp)) not in mp:
				rst.append(tmp[:])
				mp[tuple(sorted(tmp))] = True
			
			for i in range(step, n):
				tmp.append(nums[i])
				f(rst, tmp, i + 1)
				tmp.pop()
			return rst
		f(rst, tmp, step)
		return rst