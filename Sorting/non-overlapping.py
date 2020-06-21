'''
https://leetcode.com/problems/non-overlapping-intervals/
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        rst = []
        for x, y in sorted(intervals, key = lambda x: x[0]):
            if len(rst) and rst[-1][1] > x:
                cnt+=1
                rst[-1][1] = min(rst[-1][1], y)
            else:
                rst.append( [x,y] )
        return cnt