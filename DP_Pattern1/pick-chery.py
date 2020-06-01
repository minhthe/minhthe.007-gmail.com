'''
https://leetcode.com/problems/cherry-pickup/
***Noting :
using greeding method will let wrong answer.
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mp = {}
        def f(r1,c1,r2,c2):
            if (r1,c1,r2,c2) in mp:
                return mp[(r1,c1,r2,c2)]
            rst = 0 
            if r1 >=m or r2>=m or c1>=n or c2>=n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -int(1e9)
            if r1==m-1 and c1 ==n -1:
                return grid[r1][c1]
            if r2 == m -1 and c2 == n-1:
                return grid[r2][c2]
            if r1==r2 and c1==c2:
                rst +=  grid[r1][c1]
            else:
                rst += grid[r1][c1] + grid[r2][c2]
            mp[(r1,c1,r2,c2)] = rst + max(   f(r1+1,c1,r2+1,c2),  f(r1+1,c1,r2,c2+1),  f(r1,c1+1,r2+1,c2),  f(r1,c1+1,r2,c2+1)  ) 
            return mp[(r1,c1,r2,c2)]
            
        return max(0, f(0,0,0,0))