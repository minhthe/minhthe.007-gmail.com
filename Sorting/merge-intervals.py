'''
https://leetcode.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        rst= []
        if len(intervals) == 0: return None
        intervals.sort()
        x, y = intervals[0]
        
        for i,v in enumerate(intervals):
            if i == 0:
                continue
            xx, yy = v
            if y >= xx:
                y = max(yy,y)
            else:
                rst.append([x,y])
                x, y = xx , yy
        rst.append([x,y])
        return rst