import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1, n+1)}
        for src, target, time in times:
            adjList[src].append((target, time))
        
        minTime = []
        heapq.heappush(minTime, (0, k))
        shortest = {}

        while minTime:
            time, node = heapq.heappop(minTime)

            if node in shortest:
                continue
            
            shortest[node] = time

            for nodeNext, timeNext in adjList[node]:
                if nodeNext not in shortest:
                    heapq.heappush(minTime, (timeNext + time, nodeNext))
        
        print(shortest)
        if len(shortest.keys()) != n:
            return -1
        else:
            return max(shortest.values())
