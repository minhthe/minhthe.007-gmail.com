'''
[[1,5,6],[14,15,5],[4,3,3],[15,15,9],[9,2,7],[6,5,7],[19,4,4],[6,13,3],[8,16,20],[18,7,9]]
-> wrong anser 47
-> actual 48

for debug:
  '''
[[1,5,6],[14,15,5],[4,3,3],[15,15,9],[9,2,7],[6,5,7],[19,4,4],[6,13,3],[8,16,20],[18,7,9]]
-> wrong anser 47
-> actual 48
'''
if __name__=='__main__':
    
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost( costs):
        # write your code here
        
        n = len(costs)
        memo = {}
        def f(r, c):
            
            if (r, c) in memo: return memo[(r, c)]
            
            if r >= n: return 0
            # print(r,c)
            if c == 0 :
            
                x = costs[r][c] + f(r+1, c+1)
                y = costs[r][c] + f(r+1, c+2)
                z= f(r, c + 1)
                t = f(r, c+ 2)
                memo[(r,c)] = min(x,y,z,t)
                return memo[(r,c)]
                
            elif c == 1: 
                
                xx = costs[r][c] + f(r+1, c-1)
                yy = costs[r][c] + f(r+1, c+1)
                # zz= f(r, c - 1)
                # tt = f(r, c + 1)
                # memo[(r,c)] = min(xx,yy,zz,tt)
                memo[(r,c)] = min(xx,yy)
                
                return memo[(r,c)]
                
            elif c == 2:
                xxx = costs[r][c] + f(r+1, c-1)
                yyy = costs[r][c] + f(r+1, c-2)
                # zzz = f(r, c - 1)
                # ttt = f(r, c - 2)
                # memo[(r,c)] = min(xxx,yyy,zzz,ttt)
                memo[(r,c)] = min(xxx,yyy)
                
                return memo[(r,c)]
                
   
            
        ans = f(0, 0)
        return ans
    a = [[1,5,6],[14,15,5],[4,3,3],[15,15,9],[9,2,7],[6,5,7],[19,4,4],[6,13,3],[8,16,20],[18,7,9]]
    print(minCost(a))        
    
'''
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        
        n = len(costs)
        memo = {}
        def f(r, c):
            
            if (r, c) in memo: return memo[(r, c)]
            
            if r >= n: return 0
            # print(r,c)
            if c == 0 :
            
                x = costs[r][c] + f(r+1, c+1)
                y = costs[r][c] + f(r+1, c+2)
                z= f(r, c + 1)
                t = f(r, c+ 2)
                memo[(r,c)] = min(x,y,z,t)
                return memo[(r,c)]
                
            elif c == 1: 
                
                xx = costs[r][c] + f(r+1, c-1)
                yy = costs[r][c] + f(r+1, c+1)
                # zz= f(r, c - 1)
                # tt = f(r, c + 1)
                # memo[(r,c)] = min(xx,yy,zz,tt)
                memo[(r,c)] = min(xx,yy)
                
                return memo[(r,c)]
                
            elif c == 2:
                xxx = costs[r][c] + f(r+1, c-1)
                yyy = costs[r][c] + f(r+1, c-2)
                # zzz = f(r, c - 1)
                # ttt = f(r, c - 2)
                # memo[(r,c)] = min(xxx,yyy,zzz,ttt)
                memo[(r,c)] = min(xxx,yyy)
                
                return memo[(r,c)]
            
        ans = f(0, 0)
        return ans