class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #we need to remove the intervals that overlap the most

        intervals.sort()

        prevEnd = float("-inf")

        overlapping = 0
        
        for start, end in intervals:
            print(start, end)
            if start < prevEnd:

                overlapping += 1
                print(overlapping)
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
            
        
        return overlapping
