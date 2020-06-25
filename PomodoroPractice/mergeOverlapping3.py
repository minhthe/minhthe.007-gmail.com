'''
https://leetcode.com/problems/merge-intervals
'''
class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		rst = []
		for u,v in sorted(intervals):
			if len(rst) and rst[-1][1] >= u:
				rst[-1][1] = max(v, rst[-1][1])
			else:
				rst.append([u,v])
		return rst
