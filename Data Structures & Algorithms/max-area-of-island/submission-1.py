class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        maxArea = 0
        visited = set()

        def dfs(i, j):
            if (i, j) in visited or i not in range(ROWS) or j not in range(COLS):
                return 0

            if i  in range(ROWS) and j in range(COLS) and grid[i][j] == 0:
                return 0

            
            visited.add((i, j))

            res = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j-1) + dfs(i, j+1) + 1
            return res
            

            


        for i in range(ROWS):
            for j in range(COLS): 
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea