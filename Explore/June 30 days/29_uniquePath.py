''''
https://leetcode.com/problems/unique-paths/submissions/
'''
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		rst = [[1 for i in range(n)] for j in range(m)]		
		for i in range(1, m):
			for j in range(1,n):
				rst[i][j] = rst[i-1][j] + rst[i][j-1]
		return rst[m-1][n-1]