'''
https://leetcode.com/problems/all-paths-from-source-to-target/
'''
class Solution:
	def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
		
		rst = []
		n = len(graph)
		
		
		def f(tmp, p):
			if p == n -1: 
				rst.append(tmp[:])
				return 
			for ne in graph[p]:
				tmp.append(ne)
				f(tmp, ne)
				tmp.pop()
			return rst
		tmp = [0]	
		rst  = f(tmp, 0)
		return rst