'''
https://leetcode.com/problems/minimum-path-sum
'''
class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		m = len(grid)
		if m == 0 : return 0
		n = len(grid[0])
		if n== 0:return 0
		x, y = [0,1],[1, 0 ]
		mp = {}
		def f(r,c):
			if (r,c) in mp:
				return mp[(r,c)]
			if r == m -1 and c == n -1:
				return grid[r][c]
			tmp = int(1e9)
			for i in range(2):
				xx, yy = x[i] + r , y[i] + c
				if xx in range(m) and yy in range(n):
					tmp=  min(tmp, grid[r][c] + f(xx, yy))
					mp[(r,c)] = tmp
					# return tmp
			return tmp
				
		rst = f(0,0)
		return rst