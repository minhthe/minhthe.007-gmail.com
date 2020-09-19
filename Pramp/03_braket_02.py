class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        cnt = 0 
        stk = 0
        for letter in S:
            if letter == "(":
                stk += 1
            else:
                
                if stk:
                    stk -= 1
                else:
                    cnt+=1
        
        return cnt + stk