"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_data = sorted(intervals, key = lambda x:x.start)

        print(sorted_data)
        prev_end = None
        for interval in sorted_data:
            start, end = interval.start, interval.end
            print(start, end, prev_end)
            if prev_end != None  and start < prev_end:
                return False
            prev_end = end
        
        return True