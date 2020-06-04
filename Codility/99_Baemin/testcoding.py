'''

Problem #1

A Code





if __name__ == "__main__":
    
    
    nums =  [3, 1, 3, 1, 1, 3, 3, 5, 1, 3, 1]
    
    def findSingeNumber(nums):
        
        mp = {}
        for item in nums:
            mp[item] = 1 if item not in mp else mp[item] + 1 
        
        for key in mp:
            if mp[key] == 1:
                return key
                
    ans = findSingeNumber(nums)
    print(ans)
    



B Test Case

Example 1.

INPUT: [1, 1, 0, 1, 1, 1] 
OUTPUT: 0 

Example 2.

INPUT: [3, 1, 3, 1, 1, 3, 3, 5, 1, 3, 1] 
OUTPUT: 5 

Ex 3:
INPUT: [2,1,1,1,1,1] 
OUTPUT: 2 

EX 4:
INPUT: [5,5,5,5,5,6]
OUTPUT: 6

EX 5:
INPUT: [7,7,7,7,7,8] 
OUTPUT: 8



C Explanation
Logic
Using the hash map to count the frequencies of elements on the array, return the element which occurs only one time.
Performance

Time complexity: O(n), which n is the length of the array.

Space complexity: O(n), which is the hash map “mp” variable. 


Problem #2
A Code


def bfs(r, c, grid, visited, dx, dy, Rows, Cols):
    que = [(r,c,0)]
    cnt = 0
    while(len(que)):
        rr, cc, ll = que.pop(0)
        visited[rr][cc] = True
        for i in range(4):
            x, y, zz =  dx[i] + rr, dy[i] + cc, ll + 1
            if x in range(Rows) and y in range(Cols) and visited[x][y]==False and grid[x][y]==1:
                grid[x][y] = 2
                que.append((x,y, zz))
                cnt = max(cnt, zz)
    return cnt


def checkAllBlack(grid,Rows,Cols):
    for i in range(Rows):
        for j in range(Cols):
            if grid[i][j] == 1:
                return False
    return True
    
if __name__ == "__main__":
    
    grid = [[1,1,1], [1,2,1], [1,1,1]]
    
    Rows, Cols = len(grid), len(grid[0])
    
    visited = [[False for i in range(Cols)] for j in range(Rows)]
    
    def cntTheChange(grid):
        
        dx, dy = [-1,1,0,0],[0,0,-1,1]
        rst = 0
        
        
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 2 and visited[i][j] == False:
                    rst += bfs(i, j, grid, visited, dx, dy, Rows, Cols)
                    
        if checkAllBlack(grid, Rows, Cols):
            return rst * 2
        else:
            return -1
        
    ans = cntTheChange(grid)
    print(ans)
    



B Test Case

Example 1.
INPUT: [[1,1,1], [1,1,0], [0,2,1]]
OUTPUT: 6
Example 2.
INPUT: [[1,0,1], [0,1,1], [1,1,2]]
OUTPUT: -1

Example 3.
INPUT: [[0,0,0], [0,0,0], [0,0,0]]
OUTPUT: 0

Example 4.
INPUT: [[2,2,2], [2,2,2], [2,2,2]]
OUTPUT: 0

Example 5.
INPUT: [[1,1,1], [1,1,1], [1,1,1]]
OUTPUT: -1



C Explanation 
Logic

Using BFS (Breadth-First Search) to traverse. 

Firstly, start with the black item and traverse these adjacent (up, down, left, right), 

Store each changed to the Queue(first in, first out), and traverse until the queue is empty. 

Each time travels using var ‘cnt’ to get the max time, which travels to the last point of the grid.

Finally, check all items of the grid are black to return the value, if not return -1.
   
Performance

Time complexity: O(n*n), because the grid is an adjacency matrix.
 => in this problem will be O(3*3) => O(c) = 1

Space complexity: O(n*n), which n*n is the set of vertices on the grid.
 => in this problem will be O(3*3) => O(c) = 1


''''