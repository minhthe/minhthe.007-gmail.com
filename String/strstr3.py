'''
https://leetcode.com/problems/implement-strstr/
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        mp = {}
        
        mp[needle] = True
        
        m, n = len(haystack), len(needle)
        
        if n > m : return -1
        for i in range(0, m - n + 1):
            tmp = haystack[i: i+n]
            if tmp in mp:
                return i
        return -1
        