'''
https://leetcode.com/problems/reformat-the-string

Time Complexity: O(n)
Space Complexity: O(n)
'''


class Solution:
    def reformat(self, s: str) -> str:
        d = []
        c = []
        for item in s:
            if ord("a") <= ord(item) <= ord("z"):
                c.append(item)
            else:
                d.append(item)
        
        
        if(abs(len(d) - len(c)) > 1): return ""
        
        
        
        rst = ""
        
        
        if(len(d) > len(c)):
            i = 0 
            while(i < len(c)):
                rst  = rst + d[i] + c[i]
                i += 1
            rst += d[i]
        else:
            i = 0 
            while(i < len(d)):
                rst  = rst + c[i] + d[i]
                i += 1
            rst = rst + c[i] if len(c)!= len(d) else rst
        
        print(rst)
        return rst
                
            
            