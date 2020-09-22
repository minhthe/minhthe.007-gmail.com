'''https://leetcode.com/problems/car-pooling/'''
import collections
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        start_points, end_points = collections.defaultdict(int), collections.defaultdict(int)
        n = len(trips)
        min_v, max_v = int(1e9), 0
        for v,s,e in trips:
            min_v = min(min_v, s)
            max_v = max(max_v, e)
            start_points[s] += v      
            end_points[e] += v
        i, j = 0 , 0 
        
        for p in range(min_v, max_v+1):
            if p in end_points:
                capacity += end_points[p]
            
                
            if p in start_points:
                capacity -= start_points[p] 
            
            if capacity < 0: return False
            
        return True