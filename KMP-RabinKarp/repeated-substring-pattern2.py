'''
https://leetcode.com/problems/repeated-substring-pattern


***Complexity:
Time: O(n)
Space: O(n)
'''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def kmp(s):
            rst = [0] * (len(s))
            i, j = 1, 0
            while(i < len(s)):
                
                if(s[i] == s[j]):
                    j+=1
                    rst[i] = j
                    i +=1 
                else:
                    
                    if(j):
                        j = rst[j -1]
                    else:
                        rst[i] = 0
                        i += 1
            return rst
            
            
        n = len(s)
        rst = kmp(s)
        k = rst[-1] if len(rst) > 0 else 0
        return k and n % (n - k) == 0 