from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [ [1,0], [-1, 0], [0, 1], [0,-1], [1, 1], [-1,-1], [1, -1], [-1, 1]]
        
        COLS = len(grid[0])
        ROWS = len(grid)

        if grid[0][0] != 0:
            return -1

        visited = set()
        def bfs (x, y):
            queue = deque()
            queue.append( (x, y) )
            visited.add( (x, y) )

            length = 1

            while queue:

                for i in range(len(queue)):
                    coord1, coord2 = queue.popleft()

                    if coord1 == COLS -1 and coord2 == ROWS - 1:
                        return length

                    for dr1, dr2 in directions:
                        nx, ny = coord1 + dr1, coord2 + dr2

                        if 0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in visited:
                            if grid[ny][nx] == 0:
                                visited.add ( (nx, ny))
                                queue.append( (nx, ny))

                length += 1

            return -1
        return bfs (0,0)

