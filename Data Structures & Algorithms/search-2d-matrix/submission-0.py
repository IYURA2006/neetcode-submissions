class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i would go throuw each row and check whether it is in that limit and then run 
        COLS = len(matrix[0])
        ROWS = len(matrix)

        left = 0
        right = ROWS - 1

        row = 0
     
        
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][COLS - 1]:
                row = mid
                break
                

            elif matrix[mid][COLS - 1] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        print(row)

        left = 0
        right = COLS - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False