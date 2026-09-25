
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        COLS = len(grid[0])
        ROWS = len(grid)
        INF = 2**31 - 1
        NEIGHBOURS = [(1,0), (-1, 0), (0,-1), (0,1)]
        
        visited = set()

        zeros = []

        def helper():

            queue = deque()
            for items in zeros:
                queue.append(items)
                visited.add(items)

            distance = 0

            while queue:

                for _ in range(len(queue)):

                    coord1, coord2 = queue.popleft()

                    for i, j in NEIGHBOURS:
                        nx, ny = coord1 + i, coord2 + j

                        if (nx, ny) not in visited and nx in range(COLS) and ny in range(ROWS) and grid[ny][nx] != -1:
                            #if it just info we simply change it
                            if grid[ny][nx] == INF:
                                grid[ny][nx] = distance + 1
                
                            elif grid[ny][nx] != 0:
                                grid[ny][nx] = min( grid[ny][nx] , distance + 1)
                            
                            queue.append((nx,ny))
                            visited.add((nx,ny))
                                
                distance += 1

        

        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == 0:
                    zeros.append((i,j))
        
        helper()
    
