class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        COLS = len(obstacleGrid[0])
        ROWS = len(obstacleGrid)

        #edge cases
       
        unique_paths = [[0] * COLS for j in range(ROWS)]

        blocked = False

        for i in range(COLS):
            if obstacleGrid[0][i] == 1:
                blocked = True
            
            if blocked:
                unique_paths[0][i] = 0
            else:
                unique_paths[0][i] = 1
        
        blocked = False
        for i in range(ROWS):
            if obstacleGrid[i][0] == 1:
                blocked = True
            
            if blocked:
                unique_paths[i][0] = 0
            else:
                unique_paths[i][0] = 1
        
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if obstacleGrid[i][j] == 1:
                    unique_paths[i][j] = 0
                else:
                    unique_paths[i][j] = unique_paths[i-1][j] + unique_paths[i][j-1]

    
        return unique_paths[ROWS-1][COLS-1]
