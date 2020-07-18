import collections
import heapq
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        a = prerequisites
        n = numCourses
        graph = collections.defaultdict(list)
        degree=[0 for i in range(n)]
        for u, v in a:
            graph[v].append(u)
            # graph[v].append(u)
            degree[u] += 1
        zero =[i for i in range(n) if degree[i]==0]
        heapq.heapify(zero)
        rst = []
        # print(zero)
        while(len(zero)):
            u = heapq.heappop(zero)
            rst.append(u)
            # print('u',u)
            for ne in graph[u]:
                degree[ne] -= 1
                if degree[ne] == 0:
                    heapq.heappush(zero, ne)
        if len(list(item for item in degree if item == 0)) == n: 
            return rst
        return []