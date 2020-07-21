class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        if row == 0 or col == 0 : return False
        
        
        def f(r,c,pos):
            
            if pos == len(word): return True
            
            if r not in range(row) or c not in range(col)  : return False
            
            if pos < len(word) and   word[pos] != board[r][c]: return False
                                  
            board[r][c] = "*"
            
            if f(r+1,c,pos+1)  or f(r-1,c,pos+1) or f(r,c+1,pos+1) or f(r,c-1,pos+1): return True
            
            board[r][c] = word[pos]
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if f(r,c,0): return True
        return False
                        