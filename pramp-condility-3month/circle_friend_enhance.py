class Solution:
	def findCircleNum(self, M: List[List[int]]) -> int:
		n = len(M)
		
		rst = [i for i in range(n)]
		rank = [0 for i in range(n)]
		
		def findP(u):
			if rst[u] != u:
				rst[u] = findP(rst[u]) 
			return rst[u]
			
		def makeSet( u, v):
			pu , pv = findP(u), findP(v)
			if pu == pv: return 
			if rank[pu] > rank[pv]:
				rst[pv] = pu
			elif rank[pu] < rank[pv]:
				rst[pu] = pv
			else:
				rst[pu] = pv
				rank[pv] += 1
		for i in range(0, n-1):
			for j in range(i+1,n):
				if M[i][j]:
					makeSet(i,j)
		
		
		# print(rst)
		
		
		return len(list(i for i in range(n) if  rst[i]== i )) 