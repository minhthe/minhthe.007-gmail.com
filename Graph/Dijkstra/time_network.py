'''
https://leetcode.com/problems/network-delay-time
'''
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        
        graph = {}
        dist = {node : int(1e9) for node in range(1,N+1)}
        
        for u,v,w in times:
            graph[u] = graph[u] + [(w,v)] if u in graph else [(w,v)]
        pq = [(0,K)]
        heapq.heapify(pq)
        dist[K] = 0
        while(len(pq)):
            t, u = heapq.heappop(pq)
            if u in graph:
                for ne in graph[u]:
                    v1, t1 = ne[1], ne[0]
                    if t1 + t < dist[v1]:
                        dist[v1] = t1 + t
                        heapq.heappush(pq, (t1+ t, v1) )
        ans = max(dist.values()) 
        return ans if  ans < int(1e9)  else -1
        