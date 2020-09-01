'''https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island'''
class Solution:
	def minDays(self, grid: List[List[int]]) -> int:
		row = len(grid)
		col = len(grid[0])
		dx,dy =[0,0,-1,1],[-1,1, 0,0]
		def isOne():
			cnt = 0 
			track = [[ False for i in range(col) ] for j in range(row)] 
			for i in range(row):
				for j in range(col):
					if cnt==2: return False
					if grid[i][j] and track[i][j]==False:
						
						cnt +=1 
						
						stk =[(i,j)]
						
						while stk:
							
							ii,jj = stk.pop()
							track[ii][jj] = True
							for _ in range(4):
								x, y= ii+ dx[_], jj + dy[_]
								if x in range(row) and y in range(col) and track[x][y]== False and grid[x][y]: 
									stk.append((x,y))
						
			return cnt ==1 
						
			
			
		# print(isOne())	
		if not isOne(): return 0
		for i in range(row):
			for j in range(col):
				if grid[i][j]: 
					grid[i][j] = 0 
					if not isOne(): return 1 
					grid[i][j] = 1 
		return 2