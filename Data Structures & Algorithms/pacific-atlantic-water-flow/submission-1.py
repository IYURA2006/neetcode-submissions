class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        visitedPacific = set()
        visitedAtlantic = set()

        def helper(x, y, OCEAN, prevHeight):
            if not( 0 <= x < COLS ) or not(0 <= y < ROWS):
                return 
            
            if prevHeight > heights[y][x]:
                return

            if OCEAN == "PACIFIC" and (x, y) not in visitedPacific:
                visitedPacific.add((x,y))
            elif OCEAN == "ATLANTIC" and (x, y) not in visitedAtlantic:
                visitedAtlantic.add((x,y))
            else:
                return 

            helper (x + 1, y, OCEAN, heights[y][x])
            helper (x - 1, y, OCEAN, heights[y][x])
            helper (x, y + 1, OCEAN, heights[y][x])
            helper (x, y - 1, OCEAN, heights[y][x])
    
        #traverse pacific ocean (top and left)
        for x in range(COLS):
            helper(x, 0, "PACIFIC", 0)
        
        for y in range(ROWS):
            helper(0, y, "PACIFIC", 0)

        #traverse atlantic
        for x in range(COLS):
            helper(x, ROWS - 1, "ATLANTIC", 0)

        for y in range(ROWS):
            helper(COLS - 1, y, "ATLANTIC", 0)


        res = []
        for item in visitedPacific:
            if item in visitedAtlantic:
                x, y = item
                res.append([y,x])

        return res
        



