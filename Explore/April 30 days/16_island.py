'''
https://leetcode.com/problems/number-of-islands/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        r = len(grid)
        if r == 0 : return 0
        c = len(grid[0])
        dx = [-1, 1, 0 , 0]
        dy = [0, 0, -1, 1]
        visited = [[False for i in range(c)] for j in range(r)]
        cnt = 0 
        
        
        def dfs(i,j, r, c):
            stk= [(i,j)]
            while(len(stk)):
                u, v = stk.pop()
                visited[u][v] = True
                for k in range(4):
                    x , y = dx[k] + u, dy[k] + v
                    if( x in range(r) and y in range(c) and  visited[x][y] == False  and grid[x][y] == "1"):
                        stk.append((x,y))
            return 1
                
            
        for i in range(r):
            for j in range(c):
                if(grid[i][j] == "1" and visited[i][j] == False):
                    cnt += dfs(i,j ,r ,c)
        return cnt