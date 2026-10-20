import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        pass
        start = []
        end = []

        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        heapq.heapify(start)
        heapq.heapify(end)

        groups = 0

        cur_groups = 0

        while start:
            if start[0] <= end[0]:
                s = heapq.heappop(start)
                cur_groups += 1
            else:
                e = heapq.heappop(end)
                cur_groups -= 1
            
            groups = max(cur_groups, groups)

        return groups
        # end 