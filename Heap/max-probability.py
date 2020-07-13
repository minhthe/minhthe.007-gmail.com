'''
https://leetcode.com/problems/path-with-maximum-probability/
'''
import heapq
import collections
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = collections.defaultdict(list)
        k = 0 
        for u,v in edges:
            vv = succProb[k]
            k+=1
            graph[u].append( (vv, v)  )
            graph[v].append( (vv, u)  )
        dist = [int(1e9) for i in range(n)]
        
        pq = [( -1, start)]
        heapq.heapify(pq)
        dist[start] = 0
        
        while(len(pq)):
            
            v, p = heapq.heappop(pq)
            for vv, pp in graph[p]:
                if abs(vv * v) *(-1) < dist[pp]:
                    heapq.heappush(pq,   (abs(vv * v) *(-1) , pp  )  )
                    dist[pp] = abs(vv * v) *(-1) 
        ans = dist[end]
        if ans == int(1e9): return 0
        return ans * (-1)