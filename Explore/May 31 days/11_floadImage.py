'''
https://leetcode.com/problems/flood-fill
'''
class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		r, c = len(image), len(image[0])
		visited =[ [ False for i in range(c) ] for j in range(r) ]
		rst= list(map(list, image))
		def dfs(sr,sc, rst, visited, r, c, image):
		
			stk =[(sr,sc)]
			dx = [-1, 1, 0 , 0]
			dy= [0, 0, -1, 1]
			while(len(stk)):
				x, y = stk.pop()
				visited[x][y] = True
				rst[x][y] = newColor
				for i in range(4):
					u, v= dx[i] + x, dy[i] + y
					if  u in range(r) and v in range(c) and visited[u][v] == False and image[u][v] == image[x][y] :
						stk.append((u,v))
			return rst
		
		return dfs(sr,sc, rst, visited, r, c, image)