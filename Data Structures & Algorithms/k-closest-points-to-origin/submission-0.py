import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            distance = math.sqrt( (x-0)**2 + (y-0)**2 )
            heapq.heappush(distances, (distance, i))
        
        res = []
        for i in range(k):
            distance, index = heapq.heappop(distances)
            res.append(points[index])
        
        return res 