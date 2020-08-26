'''https://leetcode.com/problems/detect-cycles-in-2d-grid'''
class Solution:
	def containsCycle(self, grid: List[List[str]]) -> bool:
		
		seen = set()
		row = len(grid)
		col = len(grid[0])
		
		
		dx, dy = [0,0,-1,1], [-1,1,0,0]
		def check(x,y, parent):
			if (x,y) in seen: return True
			seen.add( (x,y) )
			
			for i in range(4):
				xx, yy = dx[i] + x, dy[i] + y
				if xx in range(row) and yy in range(col) and parent!=(xx,yy) and grid[xx][yy]== grid[x][y]:
					if check(xx,yy,(x,y)): return True
					grid[xx][yy] = 'checked'
			return False
			
			
		for i in range(row):
			for j in range(col):
				if grid[i][j] != 'checked' and check(i,j, None): return True
				grid[i][j] = 'checked'
		return False