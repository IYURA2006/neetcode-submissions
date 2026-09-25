from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        DIRECTIONS = [(1,0), (-1,0), (0, -1), (0, 1)]
        

        rotten = []
        fresh = 0

        #i would find rotten oranges
        #also the number of fresh
        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == 2:
                    rotten.append((i,j))
                
                elif grid[j][i] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        visited = set()


        def helper():
            time = -1
            rot = 0
            queue = deque()

            for items in rotten:
                queue.append(items)
                visited.add(items)
            
            while queue:
                #go by 1 sec
                for _ in range(len(queue)):
                    x, y = queue.popleft()

                    for i, j in DIRECTIONS:
                        nx, ny = x + i, y + j
                        if 0 <= nx < COLS and 0 <= ny < ROWS and (nx, ny) not in visited:

                            if grid[ny][nx] == 1:
                                grid[ny][nx] = 2
                                rot += 1
                                
                                print(time, (ny,nx))
                                queue.append((nx,ny))
                                visited.add((nx,ny))
                            

                time += 1

            return time, rot
        
        t, r = helper()
        print(r)
        if r == fresh:
            return t
        else:
            return -1
        #in the end when queue is empty check number of fresh and converted


# 1 0 1
# 0 2 0
# 1 0 1
