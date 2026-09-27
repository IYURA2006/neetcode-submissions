class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 1 -> 0 2 -> 1 3->2  3 -> 1
        #if we start at 3 - cur_preq = []
        # than we at 2 - cur_preq=[3]
        #than we at 1 -cur_preq = [3,2]

        courses = {x:[] for x in range(numCourses)}

        for prereq, desired in prerequisites:
            courses[desired].append(prereq)
    
        print(courses)


        def helper(course, prereq_list):
            if len(prereq_list) > numCourses:
                return []
            
            if course in prereq_list:
                return 

            prereq_list.add(course)
            for neighbours in courses[course]:
                    helper(neighbours, prereq_list)

            return prereq_list
        
        res = []
        for a, b in queries:
            answ = helper(b, set())
            print(answ)

            if a in answ:
                res.append(True)
            else:
                res.append(False)

        return res
     
