'''
https://leetcode.com/problems/minimum-operations-to-make-array-equal/s
'''
class Solution:
	def minOperations(self, n: int) -> int:
		arr = []
		for i in range(n):
			arr.append(  (2*i )+ 1  )
		avg = sum(arr) / n
		rst = 0 
		
		for item in arr:
			rst += abs( item - avg   )
		return int(rst // 2)