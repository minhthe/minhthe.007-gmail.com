''''
https://leetcode.com/problems/reconstruct-itinerary/
'''
import heapq
class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		
		n = len(tickets)
		graph= {}
		degree = {}
		for u,v in tickets:
			# print(u,v)
			if u not in graph:
				graph[u] = [v]
				heapq.heapify(graph[u])
			else:
			
				heapq.heappush(graph[u],v)

			if u not in degree : degree[u] = 0 
			
			
			if v in degree: degree[v] += 1 
			if v not in degree: degree[v] = 1
		
	
		ans = []
		# print(graph)
		start = 'JFK'
		def f(graph, start, ans ):
			
			if (start in graph ):
				while( len( graph[start] )):
					u = heapq.heappop(graph[start])
					# if u in graph:
					f(graph, u, ans)
				# print(start)
			ans.append(start)
		
		f(graph, start, ans )
		return ans[::-1]