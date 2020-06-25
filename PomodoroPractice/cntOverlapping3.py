'''
https://leetcode.com/problems/non-overlapping-intervals/
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        tmp = []
        
        for u, v in sorted(intervals):
            if len(tmp) > 0 and tmp[-1][1] > u:
                tmp[-1][1] = min( tmp[-1][1], v )
                cnt+=1
            else:
                tmp.append([u,v])
        return cnt