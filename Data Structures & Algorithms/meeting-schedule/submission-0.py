"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        end = -1
        i = 0
        while i < len(intervals):
            if intervals[i].start < end:
                return False
            end = intervals[i].end
            i += 1
        
        return True