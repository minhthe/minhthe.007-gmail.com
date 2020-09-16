'''https://leetcode.com/problems/min-cost-to-connect-all-points'''
import heapq
import collections
class Solution:
	def minCostConnectPoints(self, points: List[List[int]]) -> int:
	
		n = len(points)
		
		dist = [ int(1e9) for i in range(n)]
		
		pq = [(0, 0)] # -> (dist, nextpoint )
		
		heapq.heapify(pq)
		
		dist[0] = 0
		
		graph = collections.defaultdict( list )# 0 -> [( disitenct, nextpoint), ]
		
		# build the graph
		# 1 2 3 4 
		for i in range(n - 1):
			for j in range(i+1, n):
				xi, yi = points[i]
				xj, yj  = points[j]
				distance = abs(  xi - xj )  + abs(yi - yj)     #|xi - xj| + |yi - yj|
				graph[i].append(  (  distance, j ) )
				graph[j].append(  (  distance, i ) )
		# print(graph)
		# doing the prim = mst
		# 1 2 3 4 
		rst = 0 
		tracking = [False for i in range(n)]
		cnt = 0
		 
		while pq:
			d , u = heapq.heappop(pq)
			#if tracking[u] is False: rst += d
			if tracking[u] is False:
				rst += d
				cnt += 1
				if cnt  == n: return rst
			tracking[u] = True			
			for ne in graph[u]:
				dd, p = ne
				if dd < dist[p] and tracking[p] is False: 
					heapq.heappush( pq, ( dd, p ) )
					dist[p] = dd
					# tracking[u] = True
		# print(rst)
		return rst