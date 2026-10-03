"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        lastMeeting = -1
        intervals.sort(key=lambda item: item.start)

        for interval in intervals:
            start, end  = interval.start, interval.end
            if start < lastMeeting:
                return False
            lastMeeting = end
        
        return True