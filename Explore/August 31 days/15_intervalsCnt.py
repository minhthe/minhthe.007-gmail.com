'''https://leetcode.com/problems/non-overlapping-interval'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key= lambda x: x[1])
        cnt = 0 
        tmp = []
        for x, y in intervals:
            if tmp and tmp[-1][1] > x:
                cnt += 1
            if len(tmp) == 0 or  tmp[-1][1] <= x:
                tmp.append([x,y])
        return cnt