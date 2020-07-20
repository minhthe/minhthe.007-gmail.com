'''
https://leetcode.com/problems/word-search
'''
class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		row, col = len(board), len(board[0])
		if row == 0 or col == 0 : return False
		
		def check(r,c,pos):
			if pos == len(word) : return True
			
			if r not in range(row) or c not in range(col) or board[r][c] != word[pos]: return False			
					
			board[r][c]='*'
						
			if check(r+1,c,pos+1) or check(r,c+1,pos+1) or check(r-1,c,pos+1) or check(r,c-1,pos+1): return True
				
			board[r][c] = word[pos]
			return False
			
	
		for i in range(row):
			for j in range(col):
				if( board[i][j] == word[0] ):
					if check(i,j,0):
						return True
		return False