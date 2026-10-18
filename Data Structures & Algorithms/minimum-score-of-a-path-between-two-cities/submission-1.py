
from collections import defaultdict

from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjlist = defaultdict(list)

        for road in roads:
            a,b, dist = road[0], road[1], road[2]

            adjlist[a].append((b, dist))
            adjlist[b].append((a, dist))

        minDistance = float('+inf')
        
        visited = set()
        def bfs(node):
            queue = deque()
            queue.append(node)
            visited.add(node)
            nonlocal minDistance

            while queue:
                item = queue.popleft()
                
                visited.add(item)

                for neighbour, dist in adjlist[item]:
                    if neighbour != item and neighbour not in visited:
                        minDistance = min(minDistance, dist)
                        queue.append(neighbour)

        bfs(1)
        return minDistance