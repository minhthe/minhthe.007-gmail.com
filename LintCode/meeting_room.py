'''https://www.lintcode.com/problem/meeting-rooms/'''
class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda x : x.start)
        for i in range(len(intervals) - 1):
            x, y = intervals[i].start, intervals[i].end
            xx, yy = intervals[i+1].start, intervals[i+1].end
            if max(xx,x) < min(yy,y): return False
        return True