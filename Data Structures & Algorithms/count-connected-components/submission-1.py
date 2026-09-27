class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {i:[] for i in range(n)}
        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)

        visited = set()
        
        def helper(item):
            if item in visited:
                return
            
            visited.add(item)

            for neighbour in adjlist[item]:
                helper(neighbour)
        
        counter = 0
        
        for i in range(n):
            if i not in visited:
                helper(i)
                counter += 1
                print(visited)
        
        return counter
