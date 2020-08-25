'''https://leetcode.com/problems/minimum-cost-for-tickets/'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        
        def f(pos):
            if pos >= len(days):
                # memo[(pos,d)] = 0
                return 0 
            if pos in memo: return memo[pos]
            cur =days[pos] 
            cur_pos = pos
            a = costs[0] + f(pos + 1) 
            
            while  pos < len(days) -1 and days[pos+1] < cur + 7:
                pos += 1
                
            b = costs[1] + f(pos + 1)
            pos = cur_pos
            
            while pos < len(days) -1 and days[pos+1] < cur + 30:
                pos += 1
            c = costs[2] + f(pos + 1)
            pos = cur_pos
            memo[pos]= min(a,b,c)
            return memo[pos]
        
        return f(0)