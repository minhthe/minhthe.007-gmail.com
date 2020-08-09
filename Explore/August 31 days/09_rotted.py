class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_v = 0
        row , col = len(grid), len(grid[0])
        list_rot = []
        for  i in range(row):
            for j in range(col):
                if grid[i][j] == 2: list_rot.append((i,j,0))
         
        dx, dy = [-1,1,0,0],[0,0,-1,1]
        while list_rot:
            x,y,l = list_rot.pop(0)
            max_v = max(max_v, l)
            for i in range(4):
                xx,yy = dx[i] + x, dy[i] + y
                if xx in range(row) and yy in range(col) and grid[xx][yy] == 1:
                    grid[xx][yy] = 2
                    list_rot.append( (xx,yy,l+1) )
                    
        
        def check():
            return sum(list(grid[x][y]==1 for x in range(row) for y in range(col))) == 0
                    
        return max_v if check() else -1