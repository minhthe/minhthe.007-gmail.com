'''
https://www.lintcode.com/problem/longest-substring-with-at-most-two-distinct-characters/
'''
class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here
        mp = {}
        rst = 0
        start = 0 
        if len(s) == 0 : return 0
        for end in range(len(s)):
            mp[s[end]] =  mp[s[end]]  + 1 if s[end] in mp else 1 
            if len(mp) > 2 :
                rst = max(rst , end - start )
                mp[s[start]] -= 1 
                while mp[s[start]] != 0:
                    start += 1
                    mp[s[start]] -= 1
                del mp[s[start]]
                start += 1 
           
            
        
        return max(rst, end - start + 1) 