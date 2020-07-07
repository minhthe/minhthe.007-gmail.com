'''
https://www.lintcode.com/problem/meeting-rooms-ii/description
'''
# Definition of Interval.
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
    # def __str__(self):
    #     return self.start + ":" + self.end
# import deque
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort( key = lambda x: x.start)
        rst = {} 
        n = len(intervals)
        
        visited = {}
        tmp = intervals
        while(len(intervals)):
            
            item = intervals.pop(0)
            s, e = item.start, item.end
            if(s,e) not in visited: 
                visited[(s,e)] = True
                rst[(s,e)] = True
                for ii in tmp:
                    ss, ee = ii.start, ii.end
                    if (ss,ee) in visited: continue
                    if e <= ss :
                        visited[(ss,ee)] = True 
                        s ,e = ss, ee

        return len(rst.keys())
        