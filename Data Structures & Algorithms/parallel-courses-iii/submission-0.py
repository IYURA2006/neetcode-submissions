from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
       
        adjlist = {i:[] for i in range(n)}
        indegree = [0] * n
        smallestTime = [0] * n

        for prevCourse, nextCourse in relations:
            adjlist[prevCourse-1].append(nextCourse-1)
            indegree[nextCourse-1] += 1
        
        queue = deque()
        nSemesters = 0
        items = 0

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
            
        while queue:

            #process by semester
            for i in range(len(queue)):
                items += 1
                course = queue.popleft()
                smallestTime[course] = time[course] + smallestTime[course]

                for nextCourse in adjlist[course]:
                    indegree[nextCourse] -= 1
                    smallestTime[nextCourse] = max(smallestTime[nextCourse], smallestTime[course])
                    if indegree[nextCourse] == 0:
                        queue.append(nextCourse)

                        
            nSemesters +=1

        return max(smallestTime)