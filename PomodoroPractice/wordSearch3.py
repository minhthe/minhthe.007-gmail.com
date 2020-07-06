from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        mp = defaultdict(lambda : [])
        for i in range(row):
            for j in range(col):
                mp[board[i][j]].append((i,j))
        visited = [[False for i in range(col)] for j in range(row)]
        dx, dy = [-1,1,0,0],[0,0,-1,1]
        def f(x, y, s, pos):
            if len(s) ==  len(word):
                return True
            for i in range(4):
                xx, yy = dx[i] + x, dy[i] + y
                if xx in range(row) and yy in range(col) and visited[xx][yy] == False and word[pos+1] == board[xx][yy]:
                    visited[xx][yy] = True
                    if f(xx,yy,s+word[pos+1], pos+1): return True
                    visited[xx][yy] = False
            return False
                
        for x,y in mp[word[0]]:
            visited[x][y] = True
            if f( x, y, word[0], 0): return True
            visited[x][y] = False
        return False