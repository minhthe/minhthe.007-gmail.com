'''https://leetcode.com/problems/unique-paths-ii/'''
class Solution:
	def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
		m,n = len(a), len(a[0])
		rst = [[1 for i in range(n)] for j in range(m)]
		
		for i in range(m ):
			for j in range(n):
				
				if a[i][j]: rst[i][j] = 0
				elif i!=0 and j!=0: rst[i][j] =   rst[i-1][j] +  rst[i][j-1]
				elif i == 0 : rst[i][j] = rst[i][j-1]
				else: rst[i][j] = rst[i-1][j]
		return rst[m-1][n-1]
		