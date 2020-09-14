'''https://leetcode.com/problems/insert-interval/'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rst= []
        flag = True
        x, y = newInterval
        affect = False
        if len(intervals) == 0: return [newInterval]
        for i,k in enumerate(intervals):
            u,v  = k 
            if   not (( y < u )  or ( v < x) ):
                affect = True
                x ,y = min(x,u), max(y,v)
                if flag: 
                    rst.append( [x,y] )
                    flag = False
                else:
                    rst[-1] = [x,y]
            else:
                rst.append([u,v])
        u, v = rst[-1]    
        x, y =newInterval
        
        ## u v x y 
        if affect is False:
            rst.append([x,y])
            rst.sort()
        return rst