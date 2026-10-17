from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)


        visited = set()
    

        def bfs(x, y):
            queue = deque()
            queue.append((x,y))
            visited.add((x,y))

            while queue:
                i, j = queue.popleft()
                grid[j][i] = 2

                for x1, y1 in ([1,0], [-1, 0], [0, 1], [0, -1]):
                    nx, ny = i + x1, j + y1
                    if 0 <= nx < COLS and 0 <= ny < ROWS:
                        if grid[ny][nx] == 1 and (nx, ny) not in visited:
                            queue.append((nx, ny))
           
                            visited.add((nx, ny))


        def countDistances(items):
            queue = deque()

            for x, y in items:
                queue.append((x,y))

            distance = 0

            while queue:
                for q in range(len(queue)):
                    i, j = queue.popleft()

                    for x1, y1 in ([1,0], [-1, 0], [0, 1], [0, -1]):
                        nx, ny = i + x1, j + y1
                        if 0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in visited:
                            if grid[ny][nx] == 1:
                                return distance
                            queue.append((nx, ny))
                            visited.add((nx, ny))
                distance += 1

       
        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == 1:
                    bfs(i, j)
                    return countDistances(visited)
                   
