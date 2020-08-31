'''https://leetcode.com/problems/friend-circles/'''
class Solution:
	def findCircleNum(self, M: List[List[int]]) -> int:
		n = len(M)
		
		rst = [i for i in range(n)]
		
		
		def findP(u):
			while u!= rst[u]:
				u = rst[u]
			return u
			
		def makeSet( u, v):
			pu , pv = findP(u), findP(v)
			if pu == pv: return 
			rst[pu] = pv
			
		for i in range(0, n-1):
			for j in range(i+1,n):
				if M[i][j]:
					makeSet(i,j)
		
		
		# print(rst)
		
		
		return len(list(i for i in range(n) if  rst[i]== i ) )