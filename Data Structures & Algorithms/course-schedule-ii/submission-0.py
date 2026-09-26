class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i:[] for i in range(numCourses)}
        for wanted, required in prerequisites:
            courses[wanted].append(required)
        
        orderClassTaking = []
        validOrder = set()
        cur_inspecting = set()


        def dfs(course):
            if course in cur_inspecting:
                return False
            
            if course in validOrder:
                return True
            
            validOrder.add(course)
            cur_inspecting.add(course)

            for required in courses[course]:
                if not dfs(required):
                    return False

            cur_inspecting.remove(course)
            orderClassTaking.append(course)

            return True

        for x in courses:
            if not dfs(x):
                return []
        
        return orderClassTaking