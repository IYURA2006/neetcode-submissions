class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjlist = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            adjlist[a].append(b)
        
        order = []
        visited = set()
        visiting = set()


        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            
            visiting.add(node)

            

            for neighbour in adjlist[node]:
                if dfs(neighbour) == False:
                    return False

            
            visiting.remove(node)
            visited.add(node)
            order.append(node)

            return True
        
        for i in range(numCourses):
            dfs(i)

        if len(visited) != numCourses:
            return []
        else:
            return order