'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        rst = []
        mp = {  }
        for c in p:
            mp[c] = 1 if c not in mp else mp[c] + 1
        
        hs = {}
        def check(pos, s, p, hs  ):
            if len(hs):
                k= pos + len(p) -1 
                hs[ s[pos -1] ] -=1 
                hs[ s[k] ] = 1 if s[k] not in hs else hs[s[k]] + 1 
            else:
                for i in range(pos, pos + len(p)):
                    hs[s[i]] = 1 if s[i] not in hs else hs[s[i]]+1
            for key in mp:
                if key not in hs :return False
                if mp[key] != hs[key]: return False
                    
            return True
        
        

        for i in range(0, len(s) - len(p) + 1):
            if check(i, s, p, hs):
                rst.append(i)
        
        return rst
         