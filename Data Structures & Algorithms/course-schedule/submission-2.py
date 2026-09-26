class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseList = {}

        for i in range(numCourses):
            courseList[i] = []

        for desired, required in prerequisites:
            courseList[desired].append(required)
        
        path = set()
        visited = set()

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            visited.add(course)
            path.add(course)

            for neighbour in courseList[course]:
                if not dfs (neighbour):
                    return False
        
            path.remove(course)
            return True

        for i in range (numCourses):
            if not dfs(i):
                return False
        return True

            
