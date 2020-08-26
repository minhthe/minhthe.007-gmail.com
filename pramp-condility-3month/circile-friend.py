'''https://leetcode.com/problems/friend-circles'''
class Solution:
	def findCircleNum(self, M: List[List[int]]) -> int:
		
		seen = set()
		rst = 0 
		
		def dfs(i):
			seen.add(i)
			for j in range(len(M)):
				if j not in seen and M[i][j] == 1 : 
					dfs(j)
			
		for i in range(len(M)):
			if i not in seen:
				dfs(i)
				rst+=1 
		return rst