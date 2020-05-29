'''
https://leetcode.com/problems/course-schedule
'''
class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		a = prerequisites
		n  = numCourses
		graph =[[] for i in range(n)]  
		zero = []
		indegree = [0] * (n)
		for item in a:
			u, v= item[0], item[1]
			graph[u].append(v)
			indegree[v] += 1
		def f():
			
			zero = [i for i in range(n) if indegree[i] == 0] 
			while(len(zero)):
				u = zero.pop(0)
				for ne in graph[u]:
					indegree[ne] -=1 
					if indegree[ne] == 0:
						zero.append(ne)
			# print(indegree)
			for item in indegree:
				
				if item != 0: return False
			return True
		
		return f()