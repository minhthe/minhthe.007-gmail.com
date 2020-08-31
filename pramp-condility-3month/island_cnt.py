class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		
		cnt = 0 
		row = len(grid)
		if row == 0 : return cnt
		col = len(grid[0])
		if col == 0: return cnt
		def dfs(r,c):
			if not ( r  in range(row) and   c  in range(col) and  grid[r][c] == '1'):
				return
			grid[r][c] = 0
			dfs(r+1,c)
			dfs(r-1,c)
			dfs(r,c+1)
			dfs(r,c-1)
			
		for r in range(row):
			for c in range(col):
				if grid[r][c] == '1':
					dfs(r,c)
					# print(grid)
					cnt +=1
		return cnt
		