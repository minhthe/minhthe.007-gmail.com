'''
https://leetcode.com/problems/network-delay-time/

*** Edge case:

N : 1 2 3 4 -> but not provide connect with point 4
->         return ans if ans < int(1e9) and len(mp.values()) == N else -1
'''
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = {}
        dist = {node: int(1e9) for node in range(1, N+1)}
        for u, v, w in times:  
            graph[u] = graph[u] + [(v,w)] if u in graph else [(v,w)]
          
        def dfs(graph, dist):
            stk = [(K,0)]
            dist[K] = 0
            while(len(stk)):
                p, t = stk.pop()
                if p  in graph:
                    for item in graph[p]:
                        p1, t1 = item[0], item[1]
                        if t1 + t < dist[p1]:
                            dist[p1] = t1 + t
                            stk.append((p1, t1 + t))
            
            
          
        dfs(graph, dist)
        ans = max(dist.values())
        return ans if ans < int(1e9)  else -1