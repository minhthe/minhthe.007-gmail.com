'''
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree
'''
class Solution:
	def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:       
		ans =  0 
		graph = {}
		for u, v in edges:
			graph[u] = [v] if u not in graph else graph[u] + [v]
		# print(graph)
		def bfs(graph, ans):
			
			tmp  = ""
			que = [(0,0, tmp)]
			rst = []
			while(len(que)):
				s, e, tmp  = que.pop(0)
				if e : tmp += str(s) + "-" +  str(e) + "-"
				if e and hasApple[e]: rst.append(tmp)
				if e in graph:
					for ne in graph[e]:
						que.append((e, ne , tmp ))
			# print(rst)
			return rst
			
				
		
		rst = bfs(graph, ans) 
		mp = {}
		ans = 0 
		for item in rst:
			a2 =  list(x for x in item.split("-") if len(x) > 0) 
			for i in range(0, len(a2), 2):
				tmp2  =a2[i:i+2]
				h = str(tmp2[0]) + "-"+str(tmp2[1])
				# print(h)
				if h not in mp:
					mp[h] = True
					ans += 2
		# print(mp)
		return ans