'''
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence
'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mi= min(arr)
        mx = max(arr)
        n = len(arr)
        diff = ( mx - mi )//( n - 1)
        print(diff)
        mp = {}
        for item in arr:
            mp[item]  = True
        for i in range(1,n):
            mi = mi + diff
            if mi not in mp: return False
        return True
        
        