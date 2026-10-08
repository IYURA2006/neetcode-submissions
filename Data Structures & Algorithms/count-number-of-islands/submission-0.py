from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited = set()

        def bfs(i, j):
            queue = deque()
            queue.append((i,j))
            visited.add((i, j))
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy 
                    if  0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in visited:
                        if grid[ny][nx] == "1":
                            queue.append((nx,ny))
                            visited.add((nx, ny))

        counter = 0
        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    counter += 1
        return counter
