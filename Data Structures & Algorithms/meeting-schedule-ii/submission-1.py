"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        numberRooms = 0

        start = []
        end = []


        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()
        
        s = 0
        e = 0

        cur_num = 0

        print(start)
        print(end)

        while s < len(intervals) and e < len(intervals):
            if start[s] < end[e]:
                cur_num += 1
                s += 1
            elif end[e] <= start[s]:
                cur_num -= 1
                e += 1
            
            numberRooms = max(numberRooms, cur_num)

        return numberRooms