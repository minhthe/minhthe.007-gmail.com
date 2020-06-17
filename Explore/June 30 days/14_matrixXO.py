''''
https://leetcode.com/problems/surrounded-regions/
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0: return board 
        col = len(board[0])
        if col == 0: return board 
        
        visited = [[True for i in range(col)]for j in range(row)]
        mp = {}
        def f():
            stk = []
            for i in [0, row-1]:
                for j in range(0, col):
                    if board[i][j] == 'O':
                        stk.append((i,j))
            for i in [0, col-1]:
                for j in range(0, row):
                    if board[j][i] == 'O':
                        stk.append((j,i))                    
            dx, dy = [-1,1,0,0], [0,0,-1,1]
            # print(stk)
            while(len(stk)):
                u, v = stk.pop()
                mp[(u,v)] = True
                visited[u][v] = False
                for i in range(4):
                    x,y = dx[i] + u, dy[i] + v
                    if x in range(row) and y in range(col) and board[x][y] == 'O' and (x,y) not in mp:
                        stk.append((x,y))
            return visited
        visited = f()
        
        # print(visited)
        for i in range(row):
            for j in range(col):
                if visited[i][j] == False:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return board