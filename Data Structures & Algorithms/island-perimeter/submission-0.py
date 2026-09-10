
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        if not grid:
            return res

        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        counter = 0

        def helper_function(x, y):
            
            queue = deque()
            queue.append((x,y))
            visited.add((x,y))

            nonlocal counter

            while queue:
                x, y = queue.popleft()
                lines_of_cube = 4
                for i, j in directions:
                    #check if neighbouring 0 - "1" cell + 4
                    #if neigboring 1 = +3
                    #if 2 = +2
                    #if 3 += 1
                    #if 4 + = 0
                    nx, ny = x+i, y+j
                    if nx in range (COLS) and ny in range(ROWS) and grid[ny][nx] ==  1:                
                        lines_of_cube -=1
                        if ((nx,ny)) not in visited:
                            queue.append((x,y))
                            
                            print(ny,nx, lines_of_cube)

                counter += lines_of_cube
                return counter

        for i in range(ROWS):
            for j in range (COLS):
                if grid[i][j] == 1:
                    res = helper_function(j,i)
        return res
         
