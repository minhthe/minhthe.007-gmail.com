'''
https://leetcode.com/problems/flood-fill

*** enhance: not using the visited to tracking because
1) the new diffrent the old color
2) if the new == the old -> return that image
'''
class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		m = len(image)
		n = len(image[0])
		
		if newColor == image[sr][sc]: return image
		oldColor = image[sr][sc]
		dx, dy = [-1,1,0,0], [0,0,-1,1]
		
		def f(r,c):					
			image[r][c] = newColor			
			for i in range(4):
				x, y = dx[i] + r, dy[i] + c
				if x in range(m) and y in range(n) and image[x][y] == oldColor:
					f(x,y)
			return image
			
		return f(sr,sc)