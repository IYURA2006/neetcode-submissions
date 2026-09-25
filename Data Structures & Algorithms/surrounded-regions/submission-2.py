class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        def helper(x, y):
            #check the bounds and visited:
            if (x, y) in visited or not( 0 <= x < COLS ) or not (0 <= y < ROWS) or board[y][x] == "X":
                return 
            
            visited.add((x,y))

            board[y][x] = "C"

            helper(x + 1, y)
            helper(x - 1, y)
            helper(x, y + 1) 
            helper(x, y - 1)


        #top border and bottom
        for x in range(COLS):
            if board[0][x] == "O" and (x, 0) not in visited:
                helper (x, 0)
            
            if board[ROWS - 1][x] == "O" and (x, ROWS - 1) not in visited:
                helper (x, ROWS - 1)
        
       
        #left and right
        for y in range (ROWS):
            if board[y][0] == "O" and (0, y) not in visited:
                helper (0, y)
            
            if board[y][COLS - 1] == "O" and (COLS - 1, y) not in visited:
                helper (COLS - 1, y)
        

        for y in range(ROWS):
            for x in range(COLS):
                if board[y][x] == "O":
                    board[y][x] = "X"
                
                elif board[y][x] == "C":
                    board[y][x] = "O"
                
            
        