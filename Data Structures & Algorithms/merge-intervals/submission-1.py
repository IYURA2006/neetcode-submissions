class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #end point > start
        intervals.sort()

        res = []

        for interval in intervals:
            start, end = interval[0], interval[1]

            if res and res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start,end])

        return res