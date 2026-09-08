class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        visited = set()

        def dfs(y, x, counter):
            if counter == len(word):
                return True
            
            visited.add((y,x))

            for i,j in directions:
                #check it is in bound
                nx, ny = x + i, y + j
                if nx in range(cols) and ny in range(rows) and (ny, nx) not in visited:
                    #check whether match
                    if board[ny][nx] == word[counter]:
                        if dfs(ny, nx, counter + 1):
                            return True

            visited.remove((y,x))

            if len(word) == counter:
                return True
            else:
                return False

         #traverse to find entry point
        for j in range(rows):
            for i in range(cols):
                if board[j][i] == word[0]:
                    if dfs(j,i, 1):
                        return True

        return False