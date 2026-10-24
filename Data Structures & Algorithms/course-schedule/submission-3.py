from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adjlist[b].append(a)
            indegree[a] += 1

        queue = deque()
     
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        print(queue)
        count = 0
        while queue:
            item = queue.popleft()
            count += 1
            for neighbour in adjlist[item]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if count ==numCourses:
            return True
        return False