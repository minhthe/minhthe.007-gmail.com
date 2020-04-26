class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        i, j = 0 , 0
        
        def f(s1, s2, i, j, memo):
            
            if (i,j) in memo: return memo[(i,j)]
            
            if i == len(s1) or j == len(s2): 
                
                memo[(i,j)] = 0
                
                return 0
            
            if(s1[i] == s2[j]):
                
                memo[(i,j)] = 1 + f(s1, s2, i+1, j+1, memo)
            
            else:
            
                memo[(i,j)] =  max(  f(s1, s2, i+1, j, memo), f(s1, s2, i, j+1, memo) )
                
            return memo[(i,j)]
                      
        return  f(text1, text2, i, j, {})  