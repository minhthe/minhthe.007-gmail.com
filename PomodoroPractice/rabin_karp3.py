'''
https://leetcode.com/problems/implement-strstr/
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pattern = 0
        running = 0
        m = len(haystack)
        n = len(needle)
        if n > m : return -1
        for i in range(len(needle)):
            pattern += ord(needle[i])
            running += ord(haystack[i])
        for i in range(  m - n + 1):
            if pattern == running and haystack[i:i+n] == needle:
                return i
            if i + n < m:
                running += ord(haystack[i+n]) - ord(haystack[i])
        return -1
                