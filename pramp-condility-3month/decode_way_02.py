class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(s)
        memo = {}
        def f(pos):
            
            if pos in memo: return memo[pos]
            
            if pos == len(s): return 1
            
            pick_one, pick_two = 0, 0 
            
            if int(s[pos]) !=0 : pick_one = f(pos+1)
            
            
            # 123
            if pos + 1 < len(s) and  int(s[pos]) !=0 and  int(''.join(s[pos: pos +2])) <= 26: pick_two  = f(pos+2)
            memo[pos] = pick_one + pick_two
            return memo[pos]    
            
            
            
            
        return f(0)