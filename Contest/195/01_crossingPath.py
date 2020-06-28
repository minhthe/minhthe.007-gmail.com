'''
https://leetcode.com/contest/weekly-contest-195/problems/path-crossing/
'''
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mp = {}
        tmp = (0,0)
        mp[tmp] = True
        for c in path:
            u ,v = tmp
            if c == 'N':
                
                u, v= u + 1, v
                tmp = (u,v)
                if tmp in mp:return True
                mp[tmp] = True
                continue
            if c == 'S':
                u, v= u - 1, v
                tmp = (u,v)
                if tmp in mp:return True
                mp[tmp] = True
                continue                
                
            if c == 'E':
                u, v= u , v + 1
                tmp = (u,v)
                if tmp in mp:return True
                mp[tmp] = True
                continue                
            if c == 'W':
                u, v= u , v -1
                tmp = (u,v)
                if tmp in mp:return True
                mp[tmp] = True
                continue    
        return False 