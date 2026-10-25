from collections import defaultdict
from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[1,0], [-1,0], [0, 1], [0, -1]]
        COLS = len(grid[0])
        ROWS = len(grid)

        #precompute the area of islands and store it in a hashmap
        #(id : area, and keep the id in the grid)

        area_islands = defaultdict(int)

        visited = set()

        max_area = 0
        def bfs(x, y, id_island):
            nonlocal max_area
            queue = deque()
            queue.append((x,y))
            visited.add((x,y))

            while queue:
                i, j = queue.popleft()
                area_islands[id_island] += 1
                max_area = max(max_area, area_islands[id_island])
                grid[j][i] = id_island

                for X, Y in DIRECTIONS:
                    nx, ny = i + X, j + Y
                    if 0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in visited:
                        if grid[ny][nx] == 1:
                            queue.append((nx, ny))
                            visited.add((nx, ny))
        
        island_counter = 2
        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == 1:
                    bfs(i, j, island_counter)
                    island_counter += 1

        
        #going through zeros
        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == 0:
                    cur_area = 1
                    seen = set()
                    for X, Y in DIRECTIONS:
                        nx, ny = i + X, j + Y
                        if 0 <= nx < COLS and 0 <= ny < ROWS:
                            cur_island_id = grid[ny][nx]
                            if (cur_island_id not in seen):
                                cur_area += area_islands[cur_island_id]
                                seen.add(cur_island_id)
                    
                    max_area = max(cur_area, max_area)
                    
       
        return max_area 



