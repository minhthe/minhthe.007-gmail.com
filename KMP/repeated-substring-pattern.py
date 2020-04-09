'''
https://leetcode.com/problems/repeated-substring-pattern
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l < 2: return False
        
        def check(tmp, s):
            rst = tmp
            while(len(rst) < len(s)):
                rst += tmp
                if(rst != s[:len(rst)]): return False
            return True
                
        for i in range(1,len(s)//2 + 1):
            tmp = s[:i]
            if(check(tmp, s)):
                return True
        return False
            