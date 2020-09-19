'''https://leetcode.com/problems/minimum-add-to-make-parentheses-valid'''
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        cnt = 0 
        stk = []
        for letter in S:
            if letter == "(":
                stk.append(letter)
            else:
                
                if stk:
                    stk.pop()
                else:
                    cnt+=1
        
        return cnt + len(stk)