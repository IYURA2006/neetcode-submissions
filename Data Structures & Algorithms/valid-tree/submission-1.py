from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for x,y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)

        visited = set()
        path = set()
        
        def dfs(node, count, parent):
            if count > n:
                return False

            if node in path:
                return False

            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)
            
            for neighbour in adjlist[node]:
                if neighbour == parent:
                    pass
                elif not dfs(neighbour, count + 1, node):
                    return False

            path.remove(node)
            return True

        for node in range(n):
            if not dfs(node, 0, None):
                return False

            if len(visited) != n:
                return False
        return True
