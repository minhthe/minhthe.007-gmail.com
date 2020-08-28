'''
https://leetcode.com/problems/find-right-interval/
'''
class Solution:
	def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
		n = len(intervals)
		rst = [-1 for i in range(n)]
		a, b = [], []
		for i,v in enumerate(intervals):
			a.append((v[0],i))
			#b.append((v[1],i))
		a.sort()
		# b.sort()
			
		for i in range(n):
			aa,bb = intervals[i]
			left, right = 0, n - 1
			while left <= right:
				mid = int( (left + right) //2  )
				# 2 5 7 8
				if a[mid][0] >= bb  and a[mid-1][0] < bb : 						
					rst[i] = a[mid][1] 
					break
				if a[mid][0] < bb:
					left = mid + 1
				else: 
					right = mid - 1
			
		return rst
		