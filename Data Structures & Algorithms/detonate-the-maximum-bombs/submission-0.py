import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjlist = {i: [] for i in range(len(bombs))}

        for i in range(len(bombs)):
            x = bombs[i][0]
            y = bombs[i][1]
            reach = bombs[i][2]

            for j in range(len(bombs)):
                if i == j:
                    continue
                
                if math.sqrt((x - bombs[j][0]) ** 2 + (y-bombs[j][1]) ** 2 )<= reach:
                    adjlist[i].append(j)

        def dfs(node, visited):
            counter = 1
            visited.add(node)

            for neighbour in adjlist[node]:
                if neighbour not in visited:
                    counter += dfs(neighbour, visited)

            return counter


         
        max_bombs = 0
        for i in range(len(bombs)):
            visited = set()
            bombs = dfs(i, visited)

            max_bombs = max(max_bombs, bombs)
        
        return max_bombs