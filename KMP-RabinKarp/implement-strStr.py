'''
https://leetcode.com/problems/implement-strstr/
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def lps(p):
            
            arr = [0] * len(p)
            i, j = 1, 0
            
            while(i < len(p)):
                
                if(p[i] == p[j]):
                    j += 1
                    arr[i] = j
                    i += 1
            
                else:
                    
                    if(j):
                        j = arr[j-1]
                    else:
                        arr[i] = 0
                        i += 1
            return arr
    
        def f(s, p): 
            
            arr = []
            
            arr = lps(p)
            
            ls, lp = len(s), len(p)
            i, j = 0, 0
            
            while(i < ls):
                
                if(s[i]  == p[j]):
                    i += 1
                    j += 1
                if(j == lp):
                    return i - j
                elif ( i < ls and s[i] != p[j]  ):
                    if(j):
                        j = arr[j -1]
                    else:
                        i += 1
                    
                
            return -1
            
            
        return 0 if len(needle) == 0 else f(haystack, needle)
        