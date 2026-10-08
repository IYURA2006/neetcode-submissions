from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        
        indegree = {i:0 for i in range(n)}
        adjlist = {i:[] for i in range(n)}

        for x, y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        


        def bfs(nodes):
            queue = deque()
            visited = set()
            for node in nodes:
                queue.append(node)

            counter = 0

            while n - counter > 2:
                
                counter += len(queue)
                for i in range(len(queue)):

                    node = queue.popleft()
                    visited.add(node)

                    for neighbour in adjlist[node]:
                        if neighbour not in visited:   
                            indegree[neighbour] -= 1
                            if indegree[neighbour] == 1:
                                queue.append(neighbour)
        
            return queue
        
        order = []
        for key, value in indegree.items():
            if value == 1:
                order.append(key)
        
        res = bfs(order)


        return list(res)


