'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        i, j = 0, 0
        mp= {}
        rst = 0 
        while j < n :
            if s[j] in mp :
                if mp[s[j]] >= i:
                    rst = max(rst, j-i)
                    i = mp[s[j]]  +1
            mp[s[j]] = j
            j +=1
        return max(rst, j - i)