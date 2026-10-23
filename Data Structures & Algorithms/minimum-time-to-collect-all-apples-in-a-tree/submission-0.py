class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjlist = {i : [] for i in range(n)}

        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)


        total_time = 0


        def dfs(node, parent):
            #we need to process the neighbours
            #check whether they have apples add together 
            t = 0

            for neighbour in adjlist[node]:
                if neighbour != parent:
                    child_time = dfs(neighbour, node)
                    if child_time > 0 or hasApple[neighbour]:
                        t = t + child_time + 2
                        
            return t

        return dfs(0,-1)
        