'''
https://leetcode.com/problems/excel-sheet-column-number
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        l = len(s)
        
        mp = { chr( i)   : i - ord('A') + 1  for i in range(ord('A'), ord('Z')+ 1) }
        
        rst = 0
        for c in s:
            rst += mp[c] * (26)**(l-1)
            l-=1
        return rst
        
        
        