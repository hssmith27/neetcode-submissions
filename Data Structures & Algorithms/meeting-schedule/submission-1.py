"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = []
        for interval in intervals:
            heapq.heappush(times, [interval.start, interval.end])

        while times:
            cur = heapq.heappop(times)
            if not times:
                return True
            if cur[1] > times[0][0]:
                return False

        return True