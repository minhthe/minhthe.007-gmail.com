'''
https://www.lintcode.com/problem/meeting-rooms
####another clever way: 
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        # 按起点排序
        intervals = sorted(intervals, key=lambda x: x.start)
        # 要维护的最大end
        maxend = -1
        for i in intervals:
            if i.start < maxend:
                return False
            maxend = max(maxend, i.end)
        return True

'''
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        a =  sorted(intervals, key = lambda x : x.start)
        if len(a) == 0 : return True
        x , y  = a[0].start, a[0].end
        print(x, y)
        for i, v in enumerate(a):
            if i == 0: continue
            xx, yy = v.start, v.end 
            if y > xx : return False
            x , y = xx, yy
        return True