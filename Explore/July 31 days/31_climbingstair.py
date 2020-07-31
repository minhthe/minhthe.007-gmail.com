'''
https://leetcode.com/problems/climbing-stairs/
'''
class Solution:
	def climbStairs(self, n: int) -> int:
		rst = [0 for i in range(n+1)]
		rst[0], rst[1]= 1, 1
		
		for i in range(2, n+1):
			rst[i] = rst[i-1] + rst[i-2]
		return rst[n]