'''
https://leetcode.com/problems/find-the-town-judge/
'''
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        mp = {}
        m = 0
        rst = 0
        if N ==1:
            if len(trust) == 0: return 1
            return -1
        path = {}
        for u,v in trust:
            path[u] = True
            mp[v] = mp[v] + 1 if v in mp else 1
            if mp[v] > rst:
                # print('first', mp[v], m)
                # print('log',m, v, mp[v])
                m = v
                rst = mp[v]
                
        # print(mp,m)
        if mp[m] == N - 1 and m not in path: return m
        return -1