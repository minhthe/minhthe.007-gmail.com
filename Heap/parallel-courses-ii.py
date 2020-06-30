'''
https://leetcode.com/problems/parallel-courses-ii
'''
import heapq
class Solution:
	def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
		
		a = dependencies
		graph = {}
		degree = [0 for i in range(n+1)]
		degree2 = [0 for i in range(n+1)]
		for u,v in a:
			if u in graph:
				graph[u].append(v)
			else:
				graph[u] = [v]
			degree[v] += 1
			degree2[u] +=1
		
		zero = []
		gg =  {}
		for i in range(1, n+1):
			x, y, z = degree[i],  -degree2[i], i
			
			if x == 0:
				zero.append((x,y,z))
			gg[i] = x
		heapq.heapify(zero)
		cnt =  0
		d = k
		# print(graph)
		# print(zero)
		# print(gg)
		ggg = {}
		while(len(zero)):
			tt = []
			while(d > 0 ):
				d -= 1
				if len(zero) == 0: continue
				x, y, z = heapq.heappop(zero)	
				if z in graph:
					for ne in graph[z]:
						tt.append(ne)
			for item in tt:
				gg[item] -= 1
				if item not in ggg and gg[item] ==0  : heapq.heappush(zero, (0,  -degree2[item], item)  )
				if gg[item] == 0: ggg[item] = True
			cnt+=1	
			d = k
		return cnt