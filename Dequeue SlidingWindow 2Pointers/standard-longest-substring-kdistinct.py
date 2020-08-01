'''
https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters
'''
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        mp = {}
        rst = 0 
        left = 0 
        for right in range(len(s)):
            
            mp[s[right]] = mp[s[right]] + 1 if s[right] in mp else 1 
            if len(mp) > k:
                while(mp[s[left]] > 0):
                    mp[s[left]] -= 1 
                    if mp[s[left]] == 0 :
                        del mp[s[left]]
                        left += 1 
                        break
                    left += 1  
            rst = max(rst, right - left + 1)
        return rst