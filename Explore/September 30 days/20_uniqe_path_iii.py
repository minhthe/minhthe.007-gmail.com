class Solution:
	def uniquePathsIII(self, grid: List[List[int]]) -> int:
				
		r, c = len(grid), len(grid[0])
		cnt_zero = 0
		start = (0,0)
		for ii in range(r) :
			for ji in range(c):
				if grid[ii][ji] == 0: cnt_zero +=1 
				if grid[ii][ji] == 1: start = ( ii,ji )
		def f(i,j, cnt_zero):
			if  not(i in range(r) and j in range(c) and grid[i][j] != -1) : 
				return 0
						
			if grid[i][j] == 2:
				if  cnt_zero ==  -1: 
					return 1
				else:
					return 0
			grid[i][j]= -1				
			a = f(i+1,j, cnt_zero-1)
			b = f(i-1,j, cnt_zero-1)
			k = f(i,j+1, cnt_zero-1)
			d = f(i,j-1, cnt_zero-1)
			grid[i][j]= 0
			return a + b + k + d
			
		return f(start[0], start[1], cnt_zero )