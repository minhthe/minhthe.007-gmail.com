''''
https://leetcode.com/problems/happy-number/
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        mp = {}
        def f(n, mp):
            if n in mp : return False
            
            tmp = sum([int(x)**2 for x in str(n)])
            if(tmp == 1): return True
            mp[n] = True
            return f(tmp, mp)
        
        return f(n, mp)