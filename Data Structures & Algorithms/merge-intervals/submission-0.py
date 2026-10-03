import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        heapq.heapify(intervals)
        res = []
        
        while len(intervals) > 0:
            nextInterval = heapq.heappop(intervals)
            if res:
                if res[-1][1] >= nextInterval[0]:
                    res[-1][1] = max(nextInterval[1], res[-1][1])
                else:
                    res.append(nextInterval)
            else:
                res.append(nextInterval)


        return res
