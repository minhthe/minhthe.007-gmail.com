'''
https://leetcode.com/problems/minimum-path-sum/
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        if r == 0 : return 0
        
        c = len(grid[0])
        
        m = [[0 for i in range(c)] for j in range(r)]
        
        for i in range(r):
            for j in range(c):
                if i == 0 and j ==0: 
                    m[i][j]= grid[i][j]
                    continue
                elif(i == 0):
                    m[i][j] = grid[i][j] + m[i][j-1]
                    continue
                elif j == 0:
                    m[i][j] = grid[i][j] + m[i-1][j]
                    continue
                else:    
                    m[i][j] = min(m[i-1][j], m[i][j-1]) + grid[i][j]
        return m[r-1][c-1]
        