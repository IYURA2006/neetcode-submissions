from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {i:[] for i in range((numCourses))}
        indegree = [0] * numCourses
 
        for a,b in prerequisites:
            adjlist[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        res = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            item = queue.popleft()
            res.append(item)
            for neighbour in adjlist[item]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(res) != numCourses:
            return []
        else:
            return res
