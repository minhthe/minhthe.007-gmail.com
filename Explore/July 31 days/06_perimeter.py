'''
https://leetcode.com/problems/island-perimeter
'''
class Solution:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		row = len(grid)
		col = len(grid[0])
		if row == 0 or col == 0 :return 0
		
		rst = 0 
		
		visited = [[False for i in range(col)] for j in range(row)]
		dx,  dy = [0,0,-1,1], [-1,1,0,0]
		def f2(x,y):
		
			cnt = 0
			for i in range(4):
				xx, yy = dx[i] + x, dy[i] + y
				
				if xx not in range(row) or yy not in range(col):
					cnt+=1
					continue
				if grid[xx][yy] == 0:
					cnt+=1
					continue
			return cnt
		
		def f(x, y) :
			stk = [ (x,y) ]
			
			cnt = 0 
			while(len(stk)):
				x, y = stk.pop()
				cnt += f2(x,y) 
				for i in range(4):
					xx, yy = dx[i] + x , dy[i] + y
					if xx in range(row) and yy in range(col) and grid[xx][yy] == 1 and visited[xx][yy]== False:
						visited[xx][yy] = True
						stk.append((xx,yy))
			return cnt
					
					
				
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1 and visited[i][j] == False:
					visited[i][j] = True
					return f(i,j)
		return 0