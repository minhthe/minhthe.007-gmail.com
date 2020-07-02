
class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		row = len(board)
		col = len(board[0])
		if row == 0 or col == 0 : return []
		rst = []
		dx , dy = [0,0, -1, 1] , [-1, 1, 0, 0]
		
		mp = {}
		for i in range(row):
			for j in range(col):
				tmp = (i,j)
				c = board[i][j]
				if c in mp:
					mp[c].append(tmp)
				else:
					mp[c] = [tmp]
					
					
		def f( x, y, s, word, pos):
			
			if pos >= len(word):
				if word == s: return True
			
			for i in range(4):
				xx, yy = dx[i] + x, dy[i] + y
				if xx in range(row) and yy in range(col) and board[xx][yy] in mp and visited[xx][yy] == False:
					visited[xx][yy] = True
					ans = f(xx, yy, s + board[xx][yy], word, pos + 1)
					if ans: return True
					visited[xx][yy] = False
			return False
			
		for word in words:
			first = word[0]
			visited =[[False for i in range(col)] for j in range(row)] 
			if first in mp:
				for x, y in mp[afirst]:
					visited[x][y] = True
					if f(x, y, first,  word, 1):
						rst.append(word)
						break
					visited[x][y] = False
		return rst