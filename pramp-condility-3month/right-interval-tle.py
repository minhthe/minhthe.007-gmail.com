'''https://leetcode.com/problems/find-right-interval/'''
class Solution:
	def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
		n = len(intervals)
		rst = [-1 for i in range(n)]
			
		for i in range(n):
			min_v = int(1e9)
			for j in range(n):
				if i ^ j and intervals[i][1] <= intervals[j][0] and min_v >  intervals[j][0]:
					min_v = intervals[j][0]
					rst[i]= j
									
		return rst