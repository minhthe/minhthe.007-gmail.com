''''
https://leetcode.com/problems/minimum-path-sum

***be careful in these edge case :
- if elif else
- with i==0 and j==0
'''
class Solution(object):
	def minPathSum(self, grid):
		
		row = len(grid)
		if row == 0: return 0
		col = len(grid[0])
		for i in range(row):
			for j in range(col):
				if i==0 and j ==0: continue
				if i == 0 and j > 0: grid[i][j] += grid[i][j-1]
				elif j == 0 and i > 0: grid[i][j] += grid[i-1][j] 
				else: grid[i][j] += min(grid[i-1][j], grid[i][j-1])
		return grid[row-1][col-1]