'''
https://leetcode.com/problems/network-delay-time
'''
import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for x,y,z  in times:
            graph[x].append( (y,z) )
        dist = [int(1e9) for i in range(N+1) ]
        
        stk = [(0,K)]
        heapq.heapify(stk)
        dist[K] = 0 
        # print(graph)
        while(len(stk)):
            v, p  = heapq.heappop(stk)
            for pp, vv in graph[p]:
                if v + vv < dist[pp]:
                    dist[pp] = v + vv
                    heapq.heappush(stk, (dist[pp], pp))
        rst = max(dist[1:])
        if rst == int(1e9): return -1
        return rst