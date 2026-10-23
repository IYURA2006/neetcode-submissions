class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjlist = {i:[] for i in range(n)}

        for m in range(len(manager)):
            if manager[m] == -1:
                continue
            adjlist[manager[m]].append((m, informTime[manager[m]]))
        

        stack = []
        stack.append((headID, 0))
        visited = set()
        totaltime = 0
        while stack:
            
            item, cur_time = stack.pop()
            totaltime = max(cur_time, totaltime)

            for neighbour, time in adjlist[item]:
                if neighbour not in visited:
                    stack.append((neighbour, time + cur_time))
                    visited.add(neighbour)
                

        return totaltime

