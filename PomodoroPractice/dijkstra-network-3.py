'''
https://leetcode.com/problems/network-delay-time/
'''
import heapq
import collections
class Solution:
	def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
		
		graph = collections.defaultdict(list)
		for u,v,t in times:
			graph[u].append( (t,v) )
		
		
		dist = [ (1e9) for i in range(N + 1)]
		pq = [ (0, K) ]
		dist[K] = 0
		heapq.heapify( pq )
		while(len(pq)):
			v, u = heapq.heappop(pq)
			for vv, uu in graph[u]:
				if v + vv < dist[uu] :
					dist[uu] = v + vv
					heapq.heappush(pq, ( v+vv, uu )  )
		rst = max(dist[1:])
		if rst == int(1e9): return -1
		return rst