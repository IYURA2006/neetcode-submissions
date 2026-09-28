from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjlist = {i:[] for i in range(n)}
        if n == 1:
            return [0]
        indegree = [0] * n
        for a,b in edges:
            adjlist[a].append(b)
            indegree[a] += 1

            adjlist[b].append(a)
            indegree[b] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        counter = 0
        while n - counter > 2:
            
            
            #by layer
            for _ in range(len(queue)):
                leaf_node = queue.popleft()
                indegree[leaf_node] = 0
                counter += 1
                for neighbour in adjlist[leaf_node]:
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 1:
                        queue.append(neighbour)


        return list(queue)
        


