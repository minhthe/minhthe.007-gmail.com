'''
https://leetcode.com/problems/word-search
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        
        mp = {}
        for i in range(row):
            for j in range(col):
                tmp = board[i][j]
                if tmp in mp:
                    mp[tmp].append( (i,j) )
                else:
                    mp[tmp] = [(i,j)]
                    
        first = word[0]
        
        dx, dy = [-1,1,0,0], [0,0,-1,1]
        visited = [[False for i in range(col)] for j in range(row)]        
        def check(word, s, pos, n, x , y):
            
            if pos >= n -1 :
                # print('s and word', s, word, s==word)
                if s == word: 
                    
                    return True
                return False
            if word[pos] != board[x][y]: 
                return False
            for i in range(4):
                xx, yy= dx[i] + x, dy[i] + y
                if xx in range(row) and yy in range(col) and visited[xx][yy] == False and board[xx][yy] in mp :
                    
                    visited[xx][yy] = True
                    ans = check(word, s + board[xx][yy], pos + 1, n , xx, yy)
                    if ans: return True
                    visited[xx][yy] = False
            return False
            
            
        if first not in mp: return False
        for x, y in mp[first]:
            visited[x][y] = True
            if(check(word,first, 0, len(word), x, y )):
                return True     
            visited[x][y] = False
        return False
                