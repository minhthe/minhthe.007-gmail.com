'''
https://leetcode.com/problems/isomorphic-strings/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        unique = {}
        for i in range(len(s)):
           
            if s[i] not in mp:
                if t[i] in unique: return False
                mp[s[i]] = t[i]
                unique[t[i]] = True                
                     
            else:
                
                if(mp[s[i]]) != t[i]: return False
        return True