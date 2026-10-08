import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []

        #1, distance
        adjlist = {i: [] for i in range(len(points))}

        for p in range(len(points)):
            x, y = points[p][0], points[p][1]
            for i in range(len(points)):
                if i != p:
                    x2, y2 = points[i][0], points[i][1]
                    distance = abs(x - x2) + abs(y-y2)
                    adjlist[p].append([distance, i])
        
        counter = 0

        for weight, node in adjlist[0]:
            heapq.heappush(minHeap, (weight, node))
        
        visited = set()
        visited.add(0)

        while len(visited) < len(points):
            distance, node = heapq.heappop(minHeap)
  
            if node in visited:
                continue
            
            counter += distance
            visited.add(node)

            for weight, neighbour in adjlist[node]:
                if neighbour not in visited:
                    heapq.heappush(minHeap, (weight, neighbour))
        return counter