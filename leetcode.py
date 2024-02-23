class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def canAttendMeetings(intervals):
        intervals.sort(key=lambda x: x.start)
    
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True