import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        COLS = len(heights[0])
        ROWS = len(heights)

        targetX = COLS - 1
        targetY = ROWS - 1 

        visited = set()

        def bfs(x, y):
    
            queue = [(0, x, y)]
            visited = set()
        
            while queue:
                difference, X, Y = heapq.heappop(queue)

                if X == targetX and Y == targetY:
                    return difference

                if (X,Y) in visited:
                    continue

                visited.add((X, Y))

                for nx, ny in directions:
                    i, j = X + nx, Y + ny
             
                    if 0 <= i < COLS and 0 <= j < ROWS and (i, j) not in visited:
                        dif = abs(heights[Y][X] - heights[j][i])
                        heapq.heappush(queue, (max(dif, difference), i, j))
                        

        return bfs(0,0)





