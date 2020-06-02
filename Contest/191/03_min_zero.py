'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

'''
class Solution:
	def minReorder(self, n: int, connections: List[List[int]]) -> int:
		root = {}
		graph = [[] for i in range(n)]
		visited = [False for i in range(n)]
		
		for u,v in connections:
			root[(u,v)] = True
			graph[u].append(v)
			graph[v].append(u)
		def f():
			cnt = 0 
			que = [0]
			while(len(que)):
				u = que.pop(-1)
				visited[u] = True
				for ne in graph[u]:
					if visited[ne] == False:
						que.append(ne)
						if (u,ne) in root:
							cnt+=1
			return cnt
			
		ans = f()
		return ans